from databases.user import insert_user, query_user


# Updated the existing user to USERNAME_ID since it is the primary key and Emails are repeated.
def create_user(email, name, user_type):
    try:
        id_query = f'Select Max([id]) from [USERSDB].[dbo].[users]'
        result = query_user(id_query)
        user_query = f'''
        INSERT INTO [dbo].[users]
                ([id]
                ,[Email]
                ,[Name]
                ,[password]
                ,[user_permission_location]
        )
          VALUES
                ({result.values[0][0]+1}
                ,'{email}'
                ,'{name}'
                ,'RANDOM_PASSWORD'
                ,'{user_type}')
        '''
        insert_user(user_query)
        return {'message': 'User inserted successfully'}


    except Exception as e:
        raise Exception(f'Error in inserting the data into the database {e}')
