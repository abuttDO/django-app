# Storing static and media files on Spaces with Django

This example application uses Digital Ocean's [Spaces](https://www.digitalocean.com/products/spaces "You create them in your Digital Ocean account") to store `static` and `media` files for a Django project.

There are a few key steps to make this work:

1. Your app is deployed to Digital Ocean. A common way to do that is with Apps.
2. You have created a space on Spaces
3. You've got the access key, the secret, the bucket name, and the region from the space
4. Boto and a lightweight custom storage make it all work in the background.

