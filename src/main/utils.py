

def user_listings_path(instance, filename):
    return 'users_{0}/Listings/{1}'.format(instance.seller.user.id, filename)