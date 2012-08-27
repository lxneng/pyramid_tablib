Introduction
===================


This package which provides custom renderer factory(xlsx, xls, csv) for
Pyramid.


Getting Started
--------------------

Include pyramid_tablib either by setting your includes in your .ini, or by calling `config.include('pyramid_tablib')`.

::
    pyramid.includes =
        pyramid_tablib

Now in your view

::
    @view_config(route_name='users+xlsx', renderer='xlsx')
    def all_users(request):
        headers = ['Name', 'City', 'Email']
        data = [(user.name, user.city, user.email) for user in users]
        return {'data': data, 'headers': headers}
