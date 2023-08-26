import boto3

def rotate_keys(event, context):
    # Inicialize o cliente IAM
    iam = boto3.client('iam')
    
    # Liste todos os usuários IAM
    all_users = iam.list_users()['Users']
    
    # Filtra usuários com base em tags
    for user in all_users:
        user_name = user['UserName']
        
        # Obtém tags do usuário
        tags = iam.list_user_tags(UserName=user_name)['Tags']
        
        # Verifica se o usuário tem uma tag específica
        should_rotate = any(tag['Key'] == 'RotateKeys' and tag['Value'] == 'True' for tag in tags)
        
        if should_rotate:
            # Liste as chaves existentes
            existing_keys = iam.list_access_keys(UserName=user_name)['AccessKeyMetadata']
            
            # Crie uma nova chave
            new_key = iam.create_access_key(UserName=user_name)
            
            # Desative as chaves antigas
            for key in existing_keys:
                iam.delete_access_key(UserName=user_name, AccessKeyId=key['AccessKeyId'])

            print(f"Chaves rotacionadas com sucesso para o usuário {user_name}")

