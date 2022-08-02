- **Descrição**: O plugin **Typescript OpenAPI** permite a criar uma Lambda com base em um arquivo de especificação **OpenAPI**.
- **Categoria**: App
- **Stack:** Lambda
- **Criado em**: 11/02/2022
- **Última atualização**: 13/06/2022
- **Download:** [app-typescript-openapi-plugin](https://github.com/stack-spot/app-typescript-openapi-plugin)

# Índice  
- [Visão Geral](#Visao-Geral)
- [Uso](#Uso)
  - [Pré-requisitos](#Pre-requisitos)
  - [Recomendado](#Recomendado)
  - [Configuração do STK CLI](#Configuração-Stack-CLI)
    - [Verificação de Template e Plugin](#Verificacao_template_e_plugin)
  - [Instalação](#Instalacao)
- [Tutorial](#Tutorial)
- [Useful commands](#Useful-commands)
- [Next Steps](#Next-steps)

## **Visão Geral**  
### **Funcionamento do Typescript OpenAPI Plugin**  
Por meio das linhas de comando da StackSpot (STK CLI) é possível aplicar o plugin em uma aplicação do tipo **APP**.

Ao aplicar o Template de **_construct_**, o **cdk** é criado na aplicação, utilizando o componente **`@stackspot/cdk-component-openapi-typescript`**.  

Durante a aplicação do Plugin, um código Lambda é gerado baseado na especificação **OpenAPI**, definida no arquivo **`infra/spec/{{spec_file_name}}.yaml`**. 

## **Uso**  
Esta seção mostra como utilizar o Plugin por meio do STK CLI, criando uma aplicação baseada no Template [**app-typescript-template**](https://github.com/stack-spot/app-typescript-template).

Depois de criar a aplicação é possível aplicar o Plugin **`app-typescript-openapi-plugin`**.   

### **Pré-requisitos**  
É preciso ter as configurações abaixo para utilizar o Plugin:    
- [**Instalar o STK CLI**](https://docs.stackspot.com/v3.0.0/os-cli/installation/);  
- [**NodeJS**](https://nodejs.org/en/);  
- [**Git**](https://git-scm.com/);  
- [**AWS CLI**](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html);  
- [**CDK**](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html);  

> É recomendando também usar o [**LocalStack**](https://github.com/localstack/localstack) como ferramenta de desenvolvimento. 

### **Configuração do STK CLI**  
Execute o comando abaixo para atualizar o local com o catálogo que tem o **`OpenAPI Plugin`**:    

```bash
stk add stack https://github.com/stack-spot/crystal-typescript-api-stack
```

#### **Verificação do Template e Plugin**    
Executando os comandos abaixo é possível verificar se o catálogo foi carregado localmente.

**Listagem de Plugins disponíveis localmente:**

```bash
stk list plugin
```

**Exemplo de output:**  
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

**Listagem de Templates disponíveis localmente:**
```bash
stk list template
```

**Exemplo de output:**
```bash
Stack: crystal-typescript-api-stack
+----------------------+---------------------------------------------+------------------+-----------------+
| name                 | description                                 | types            | version(latest) |
+----------------------+---------------------------------------------+------------------+-----------------+
| base-app-ts-template | Base template to work with typescript stack | ['app-template'] | no release      |
|                      |                                             |                  |                 |
+----------------------+---------------------------------------------+------------------+-----------------+
```

### **Instalação**  
Siga os passos a passo abaixo para criar e configurar o Plugin na sua aplicação:    

**Passo 1.** Copie e cole a URL abaixo no seu terminal:

```bash
stk create app meu-teste-app -t crystal-typescript-api-stack/base-app-ts-template
```

**Passo 2.** Acesse o projeto criado:  

```bash
cd meu-teste-app
```

**Passo 3.** Aplique o Plugin baseado em catálogo: 
 
```bash
stk apply plugin crystal-typescript-api-stack/app-typescript-openapi-plugin
```

### Inputs
Os inputs necessários para utilizar o Plugin são:  

| Campo                              | Tipo | Descrição                                                                                                                         | Valor Padrão       |
| :---                               | :--- | :---                                                                                                                              | :---               |
| *api_name*                         | text | Define o nome da API e também é utilizado para fazer o link de códigos gerados e referências de código.                              | api-name           |
| *import_spec_file*                 | bool | Define se o usuário deseja importar um arquivo de especificação OpenAPI.                                                          | True               |
| *import_spec_file_path*            | text | Define o o caminho para o arquivo de especificação que será importado. Obs.: só se o **import_spec_file** for **True** |                    |
| *spec_file_name*                   | text | Define o nome do arquivo de especificação OpenAPI localizado no diretório /spec. Por padrão é `spec-file-name`.                     | spec-file-name     |
| *source_dir*                       | text | Define o caminho, a partir da raiz do projeto, dos arquivos OpenAPI Lambda gerados. Por padrão é `src`.                             | src                |
| *access_control_allow_origin*      | text | Define a utilização de `Access-Control-Allow-` customizado dos endpoints.                                                     | *                  |
| *access_control_allow_headers*     | text | Define a utilização de `Access-Control-Allow-Headers` customizado dos endpoints.                                                    | *                  |
| *access_control_allow_methods*     | text | Define a utilização de `Access-Control-Allow-Methods` customizado dos endpoints.                                                    | *                  |
| *access_control_allow_credentials* | text | Define a utilização de `Access-Control-Allow-Credentials` customizado dos endpoints.                                                | *                  |

## **Tutorial**  
Depois de criar e aplicar o Plugin, é possível fazer o deploy da aplicação _Lambda_ gerada. 

### **1. CDK bootstrap**
Execute o _CDK bootstrap_ abaixo para preparar a Stack e gerar os arquivos do serviço: 

```
cdk bootstrap --profile <your-aws-profile>
```

#### **Problema relacionado ao acesso público do S3**  
Se houver problema de configuração de acesso público bloqueado ao S3, na execução do comando _bootstrap_ é possível solucionar com a opção `--public-access-block-configuration false`. Confira o exemplo abaixo:  

```
cdk bootstrap --profile <your-aws-profile> --public-access-block-configuration false
```
> Obs.: Se utilizar _npm run cdk bootstrap_, é necessário adicionar `--` após o comando `bootstrap`:  
> ```
> npm run cdk bootstrap -- --public-access-block-configuration false
> ```

#### CDK Local
Este Plugin configura automaticamente, para ambiente de desenvolvimento, o uso de _CDK Local_.

Para usar _LocalStack_ e fazer o bootstrap localmente, execute o comando abaixo:  

```
npm run local bootstrap
```

### **2. Alterar o retorno do endpoint**
Edite o arquivo _usecase_ gerado (`{{source_dir}}/post-hello/usecase.ts`) e implemente o código para gerar uma resposta esperada com o _import_ `{{source_dir}}/api-models.ts`. Confira o exemplo abaixo:  

```javascript
import { HelloRequest, HelloResponse } from '../api-schemas';

export type PostHelloParams = {
  requestBody: HelloRequest,
};

export const postHello = async ({ requestBody }: PostHelloParams): Promise<HelloResponse> => {
  return {
    greeting: `Hello ${requestBody.name}!`,
  };
};
```

### **3. Build, deploy e chamada da API**  
Execute `npm run build`, `cdk deploy` e faça uma chamada com _curl_ ao endpoint criado, com o _payload_ apropriado. Confira o exemplo abaixo:  

```
npm run build
cdk deploy
curl -X POST -H 'Content-Type: application/json' -d '{"name": "USERNAME"}' https://mhi8zrb3c7.execute-api.us-east-1.amazonaws.com/prod/hello
```

> Parabéns! Você criou sua API baseada em uma especificação OpenAPI, realizou o deploy dela na AWS e já esta configurada com a API Gateway e Lambda!  

## **Comandos Úteis**  

**Comando**   | **Descrição**
--------- | ------
`npm run build`| Compila typescript para jsii.
`npm run watch` | Observa as mudanças e as compila.
`npm run test` | Executa os testes unitários com jest.
`npm run coverage` | Executa a cobertura de testes. 
`npm run local synth` | Sintetiza o projeto CDK com _cdk local_ e gera/atualiza o projeto.
`npm run local deploy` | Faz o deploy para o localstack
`npm run cdk synth` | Sintetiza o projeto CDK com _cdk_ e gera/atualiza o projeto.
`npm run cdk deploy` | Faz o deploy para a conta AWS configurada.

## **Próximos passos**  

Depois de aplicar o Plugin OpenAPI, ao editar o arquivo `{{spec_file_name}}.yaml`, é possível atualizar os arquivos baseados nesta especificação. 
