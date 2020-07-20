import requests
import hashlib
import sys


# #############
# url = 'https://api.pwnedpasswords.com/range/' + 'password123'
# # we only write 5 charakters of our hash password (example below)
# # 2
# url_2 = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
# # CBFDAC6008F9CAB4083784CBD1874F76618D2A97(hash password of password123)

# res = requests.get(url)
# res2 = requests.get(url_2)
# print(res)  # give response 400
# print(res2)  # give response 200
# # so the response should be 200 so the example 2 is better

# ############


def request_api_data(query_char):
    # instead the 5 hash charakter of the password we can write query_char
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:  # should be 200 if otherwise write err
        raise RuntimeError(
            f'Error fetching: {res.status_code} check the api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:  # checking how many time my password was leaks
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    # from 0 to 5 and from 5 to end
    response = request_api_data(first5_char)
    # print(first5_char, tail)
    # print(response)  # if every function is ok we should have response 200
    # return response
    return get_password_leaks_count(response, tail)

# pwned_api_check('password123')
# pwned_api_check('123')


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f'{password} was found {count} times... you should probably change the password!')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'All done!'

#    main(sys.argv[1:])


if __name__ == '__main__':  # run this file if is the main running file with command line
    # sys.exit means that the program was finished
    sys.exit(main(sys.argv[1:]))



'''
to run in command line write:
python(or python3) <script> <argument> <argument2> ...
python passwordchecker.py abc123 password123 123 #we check these 3 password how many timer they are leaks
'''