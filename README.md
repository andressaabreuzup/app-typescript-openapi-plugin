## Descrição
O plugin Typescript OpenAPI permite a criação de Lambda com base em um arquivo de especificação OpenAPI.

- **Descrição:** Adicione uma descrição curta sobre o que é o plugin.  
  O plugin xxx é um xxx e permite xxx.

- **Categoria:** ?Insira a categoria.?
- **Stack:** ?Lambda?
- **Criado em:** 11/02/2022
- **Última atualização:** 11/02/2022
- **Download:** [app-typescript-openapi-plugin](https://github.com/stack-spot/app-typescript-openapi-plugin)

## Visão Geral
### Typescript OpenAPI Plugin
Insira um resumo do plugin. Responda as perguntas: o que ele faz e como funciona.  
Sugerimos um texto para você iniciar:  
O **xx plugin** é um serviço de filas e permite a escalabilidade de microserviços.

### Como Typescript OpenAPI Plugin funciona
Explique como esse plugin funciona e adicione imagens/infográficos/diagramas da arquitetura para facilitar a compreensão.

## Uso
TODO  

### Pré-requisitos
Adicione os pré-requisitos que a pessoa usuária precisa ter antes de utilizar o plugin.

Para utilizar esse plugin, é necessário:
- [**GitHub**](www.github.com)
- [**adicione a ferramenta**](Link.com)

### Instalação
Nesta subseção, adicione a URL de download e coloque os passos para a instalação, se necessário.

Para fazer o download do **plugin xx**, siga os passos abaixo:

**Passo 1.** Copie e cole a URL abaixo no seu navegador/terminal:
```
url plugin
```
**Passo 2.** xxx

## Configuração
Nesta subseção, é necessário adicionar as informações das configurações que a pessoa usuária precisa fazer para utilizar o plugin.

## Tutorial

1. Execute CDK bootstrap to prepare stack and generate service stubs  
```
cdk bootstrap --profile <your-aws-profile>
```

### Problem related to S3 public access
If you have permissions problems related to S3 public access block configuration permissions on bootstrap you could add the option `--public-access-block-configuration false` to the bootstrap command as shown below:  
```
cdk bootstrap --profile <your-aws-profile> --public-access-block-configuration false
```

### CDK Local
This plugin configures automatically (for DEV environment) the use of _CDK Local_  
To use LocalStack and do a local bootstrap execute the command below:  
```
npm run local bootstrap
```

2. Edit generated usecase stub (`{{source_dir}}/post-hello/usecase.ts`) and implement the code to generate the expected response imported from `{{source_dir}}/api-models.ts` as shown below:  
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

3. Run `npm run build`, `cdk deploy` and call api at the endpoint created with an appropriate payload.

```
npm run build
cdk deploy
curl -X POST -H 'Content-Type: application/json' -d '{"name": "USERNAME"}' https://mhi8zrb3c7.execute-api.us-east-1.amazonaws.com/prod/hello
```

Congratulations! You created your API based on an OpenAPI specification and deployed it at AWS with API Gateway and Lambda!

## Useful commands

- `npm run build` compile typescript to jsii
- `npm run watch` watch for changes and compile
- `npm run test` perform the jest unit tests
- `npm run package` package library using jsii
- `npm run coverage` run tests with coverage reports
- `npm run local synth` synthesize CDK project with _cdk local_ and generate/update service stubs
- `npm run local deploy` deploy build _lamba_ to localstack

## Next steps

After OpenAPI Plugin has been applied, editing the file `{{spec_file_name}}.yaml` enables update the generated service stubs based on this file  

