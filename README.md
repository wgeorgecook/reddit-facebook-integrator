# Reddit to Facebook Integrator

## Introduction
Finally, the Facebook "plugin" you've been needing but never knew existed! If you're like me, you have one friend that you send all the cool stuff you find Reddit. This application will do just that.

## Background
This integration is written in Python and requires a cron job to start the app and check for any updates. It will first check your latest **upvoted** post and compare it against a database of updated posts. If the latest post and the last post in the database are the same, it will pass. If a unique post is found, it will share the link with a friend you designate in `settings.py` under "desired_username".

## Deployment
I highly suggest downloading [Vagrant](https://vagrantup.com), as the deployment scripts in `/deployment` will work out the box. Once you've got Vagrant installed locally, clone this repository and `cd` into `/deployment`. From there, run `vagrant up` and the Vagrantfile will download a copy of Ubuntu server, download the required apt packages, and create a virtual Python environment. Pip packages in `/deployment/requirements.txt` will then install.

## Facebook and Reddit API Info
You will need to get your own [Facebook Developer](https://developers.facebook.com/) and [Reddit Developer](https://www.reddit.com/dev/api/) account. Rename the `settings_template.py` file to `settings.py` and populate the requisite keys with the required values for client and API tokens.

## Database
As mentioned above, upvoted Reddit posts are stored in a PostgreSQL database. This gets automatically congiured using `pg_hba.conf` and `psql_setup.sql`. If you make changes to the database or table names, make sure to update them in `settings.py` as well.

## Contributing
This was a fun project that I don't have in deployment anymore, but I think it could have so much more potential. If you want to fork this and implement some fun new features, please do so! Submit a detailed pull request with the changes you made and how they affect the core functionality and after review I will merge into `master`.