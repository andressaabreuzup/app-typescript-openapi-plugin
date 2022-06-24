## Uso
Nessa seção mostra como é feita a utilização do plugin por meio do CLI, criando uma aplicação baseada no template [**app-typescript-template**](https://github.com/stack-spot/app-typescript-template)  
Após a criação da aplicação é possível aplicar o plugin **app-typescript-openapi-plugin**  

### Pre-requisitos
Necessário a configuração de alguns pré-requisitos para utilização do plugin.  
- [**Instalação StakSpot CLI**](https://docs.stackspot.com/v3.0.0/os-cli/installation/)
- [**NodeJS**](https://nodejs.org/en/)
- [**Git**](https://git-scm.com/)
- [**AWS CLI**](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
- [**CDK**](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

### Recomendado
Recomendamos a utilização de algumas ferramentas para desenvolvimento  
- [**LocalStack**](https://github.com/localstack/localstack)

### Configuração Stack CLI
Executar comando abaixo para atualização de local com catálogo que contém OpenAPI plugin:  
```bash
stk add stack https://github.com/stack-spot/crystal-typescript-api-stack
```

#### Verificacao template e plugin
Executando os comandos abaixo é possível verificar que o catálogo foi carregado localmente  
**Listagem plugin disponíveis localmente:**
```bash
stk list plugin
```

**Exemplo output:**
```bash
Stack: crystal-typescript-api-stack
+-----------------------------------+-------------------------------------------------------------------------------------------+---------+-----------------+
| name                              | description                                                                               | types   | version(latest) |
+-----------------------------------+-------------------------------------------------------------------------------------------+---------+-----------------+
| app-typescript-openapi-plugin     | Plugin that applies contract first driven by an OpenAPI contract and auto generate source | ['app'] | 0.1.0           |
|                                   | codes for lambdas and the nested CDK infrastructure                                       |         |                 |
|                                   |                                                                                           |         |                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+---------+-----------------+
```

**Listagem template disponíveis localmente:**
```bash
stk list template
```

**Exemplo output:**
```bash
Stack: crystal-typescript-api-stack
+----------------------+---------------------------------------------+------------------+-----------------+
| name                 | description                                 | types            | version(latest) |
+----------------------+---------------------------------------------+------------------+-----------------+
| base-app-ts-template | Base template to work with typescript stack | ['app-template'] | no release      |
|                      |                                             |                  |                 |
+----------------------+---------------------------------------------+------------------+-----------------+
```

### Instalacao
Os passos dessa seção mostram como criar e configurar o plugin na aplicação  

**Passo 1.** Copie e cole a URL abaixo no seu terminal:
```bash
stk create app meu-teste-app -t crystal-typescript-api-stack/base-app-ts-template
```

**Passo 2.** Acessar projeto criado:  
```bash
cd meu-teste-app
```

**Passo 3.** Aplicação de plugin baseado em catálogo:  
```bash
stk apply plugin crystal-typescript-api-stack/app-typescript-openapi-plugin
```

### Inputs
Abaixo estão listados os inputs do plugin.

Os inputs necessários para utilizar o plugin são:  

| Campo                              | Tipo | Descrição                                                                                                                         | Valor Padrão       |
| :---                               | :--- | :---                                                                                                                              | :---               |
| *api_name*                         | text | Define o nome da API, também utilizado para fazer o link de códigos gerados e referências de código.                              | api-name           |
| *import_spec_file*                 | bool | Define se o usuário deseja importar um arquivo de especificação OpenAPI.                                                          | True               |
| *import_spec_file_path*            | text | Define o o caminho para o arquivo de especificação que será importado. Obs.: apenas utilizado se **import_spec_file** for **True** |                    |
| *spec_file_name*                   | text | Define o nome do arquivo de especificação OpenAPI localizado no diretório /spec, por padrão é spec-file-name.                     | spec-file-name     |
| *source_dir*                       | text | Define o caminho, a partir da raiz do projeto, dos arquivos OpenAPI lambda gerados, por padrão é src.                             | src                |
| *access_control_allow_origin*      | text | Define a utilização de Access-Control-Allow-Origin customizado dos endpoints.                                                     | *                  |
| *access_control_allow_headers*     | text | Define a utilização de Access-Control-Allow-Headers customizado dos endpoints.                                                    | *                  |
| *access_control_allow_methods*     | text | Define a utilização de Access-Control-Allow-Methods customizado dos endpoints.                                                    | *                  |
| *access_control_allow_credentials* | text | Define a utilização de Access-Control-Allow-Credentials customizado dos endpoints.                                                | *                  |
