from faker import Faker
from collections import namedtuple
import random, time, datetime
fake = Faker()

# Question: 1

def namedtuple_profile(n):
    '''This function should take n as an integer and will create n no of profiles in a tuple of namedtuples and
    from there it will return blood group with max frequency, mean location of all profiles address,
    maximum age and average age.'''
    profile = namedtuple('profile',fake.profile().keys())
    f_profile = tuple([profile(**fake.profile()) for i in range(n)])
    blood_freq = dict()
    blood_grp_list = [profile.blood_group for profile in f_profile]
    {w: 1 if w not in blood_freq and not blood_freq.update({w: 1}) else blood_freq[w] + 1 if \
        not blood_freq.update({w: blood_freq[w] + 1}) else 1 for w in blood_grp_list}
    max_blood_grp_count = list(blood_freq.keys())[list(blood_freq.values()).index(max(blood_freq.values()))]
    mean_loc = sum([profile.current_location[0] for profile in f_profile])/n,sum([profile.current_location[1]\
        for profile in f_profile])/n
    all_age = [(datetime.datetime.today().date() - profile.birthdate).days for profile in f_profile]
    max_age = max([(datetime.datetime.today().date() - profile.birthdate).days for profile in f_profile])
    avg_age = sum(all_age)/n
    return max_blood_grp_count, mean_loc, max_age, avg_age

# Question 2:

def dict_profile(n):
    '''This function should take n as an integer and will create n no of profiles in a list of dictionaries and
    from there it will return blood group with max frequency, mean location of all profiles address,
    maximum age and average age.'''
    f_profile = [fake.profile() for i in range(n)]

    blood_freq = dict()
    blood_grp_list = [profile['blood_group'] for profile in f_profile]
    {w: 1 if w not in blood_freq and not blood_freq.update({w: 1}) else blood_freq[w] + 1 if\
        not blood_freq.update({w: blood_freq[w] + 1}) else 1 for w in blood_grp_list}
    max_blood_grp_count = list(blood_freq.keys())[list(blood_freq.values()).index(max(blood_freq.values()))]

    mean_loc = sum([profile['current_location'][0] for profile in f_profile])/n,\
        sum([profile['current_location'][1] for profile in f_profile])/n

    all_age = [(datetime.datetime.today().date() - profile['birthdate']).days for profile in f_profile]

    max_age = max(all_age)

    avg_age = sum(all_age)/n

    return max_blood_grp_count, mean_loc, max_age, avg_age

def perf_chek():
    '''This function should check the performance of the above two functions and return timediff between two'''
    start2 = time.perf_counter()
    for i in range(2):
        _,_,_,_ = dict_profile(10000)
    end2 = time.perf_counter()
    delta2 = end2-start2

    start1 = time.perf_counter()
    for i in range(2):
        _,_,_,_ = namedtuple_profile(10000)
    end1 = time.perf_counter()
    delta1 = end1-start1

    return delta2 - delta1

# Question 3:

company = namedtuple('company','company_name symbol open high close')

def create_company_tuple():
    ''' This function creates a namedtuple object of a company name, symbol,
    company stock open, high and close price.
    we have created open value as random no between 10 and 4000. 
    High value should range from 90% to 110% of open value
    and close value should range from 90% to 100% of high value'''

    company_name = fake.company()

    symbol = company_name[0:4].upper()

    open = random.randint(10,4000)

    high = int(open * random.uniform(1,1.2))

    close = int(high * random.uniform(0.9,1))

    return company(company_name,symbol,open,high,close)

def stock_market(n):
    '''This function takes an integer as an input and creates namedyuple of n no of fake companies
    and calculates open high and close price of whole stock market with n no of companies and 
    returns a namedtuple of whole stockmarket's open close high and close price details'''
    company_tuple = namedtuple('company_tuple',list(range(n)),rename=True)

    weight_list = [round(random.uniform(0,1),2) for i in range(n)]
    weight = namedtuple('weight',list(range(n)),rename=True)
    normalized_weight = weight._make([i/sum(weight_list)for i in weight_list])

    stock = namedtuple('stock',company._fields + ('stock_weight',))

    ct = company_tuple._make([stock(*create_company_tuple(),normalized_weight[i]) for i in range(n)])

    stock_market_details = namedtuple('stock_market_details','open high close')
    market_open, market_high, market_close = 0,0,0
    for i in range(len(ct)):
        market_open += (ct[i].open * ct[i].stock_weight)
        market_high += (ct[i].high * ct[i].stock_weight)
        market_close += (ct[i].close * ct[i].stock_weight)

    return stock_market_details(open = market_open, high = market_high, close = market_close)


