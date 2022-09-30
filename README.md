# Storing static and media files on Spaces with Django

This example application uses Digital Ocean's [Spaces](https://www.digitalocean.com/products/spaces "You create them in your Digital Ocean account") to store `static` and `media` files for a Django project.

There are a few key steps to make this work:

1. Your app is deployed to Digital Ocean. A common way to do that is with Apps.
2. You have created a space on Spaces
3. You've got the access key, the secret, the bucket name, and the region from the space
4. Boto and a lightweight custom storage make it all work in the background.


## Getting started with this repo

Create a virtual environment, install dependencies, and migrate. Assumes you've got a `DATABASE_URL` in your environment variables.


    $ virtualenv -p python3.10 env
    $ source env/bin/activate
    $ pip install -r requirements
    $ python manage.py migrate

## Next, step up your Spaces on Digital Ocean

1. Create a new space (also called a bucket)
2. Choose a region close to where most of your users are, I chose NYC 3
3. Give it a name that makes sense for what's in your space
4. When it's created, go back to Spaces and click `Manage Keys`
5. Under "Spaces access keys" click the button to `Generate New Key`
6. Give it a name. When it's generated, **BE SURE** to copy the secret and the access key.
7. You should now have the information to create 4 environment variables:
    1. `SPACES_ACCESS_KEY`
    2. `SPACES_SECRET_KEY` this is only shown **once** when you create your keys
    3. `SPACES_BUCKET` this is the friendly name you gave your bucket in step #3 above
    4. `SPACES_REGION_NAME` you should see this in your spaces url, something like `nyc3` as part of `bucket-name.nyc3.digitaloceanspaces.com`
8. Once those environment variables are in, your custom backend is effectively configured.
