- **Description**: Typescript OpenAPI plugin allows the creation of Lambda based on an OpenAPI specification file.
- **Category**: App
- **Stack:** Lambda
- **Created in**: 11/02/2022
- **Last update**: 13/06/2022
- **Download:** [app-typescript-openapi-plugin](https://github.com/stack-spot/app-typescript-openapi-plugin)

# Summary
- [Overview](#Overview)
- [Use](#Use)
  - [Requirements](#Requirements)
  - [Recommended](#Recommended)
  - [Stack CLI](#Stack-CLI)
    - [Template and plugin verification](#Template-and-plugin-verification)
  - [Install](#Install)
- [Tutorial](#Tutorial)
- [Useful commands](#Useful-commands)
- [Next Steps](#Next-steps)

## Overview
### How Typescript OpenAPI Plugin works
Through the StackSpot command lines, it is possible to apply the plugin in an APP type application.
When executing the application, the _construct_ cdk template is created in the application, using the component `@stackspot/cdk-component-openapi-typescript`.  
During the application of the plugin, the Lambda code is generated based on the OpenAPI specification defined in the file `infra/spec/{{spec_file_name}}.yaml`.

## Use
This section shows how the plugin is used through the CLI, creating an application based on the template [**app-typescript-template**](https://github.com/stack-spot/app-typescript-template).  
After creating the application it is possible to apply the plugin **app-typescript-openapi-plugin**.

### Requirements
It is necessary to configure some prerequisites to use the plugin.
- [**Install the StakSpot CLI**](https://docs.stackspot.com/v3.0.0/os-cli/installation/)
- [**NodeJS**](https://nodejs.org/en/)
- [**Git**](https://git-scm.com/)
- [**AWS CLI**](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
- [**CDK**](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

### Recommended
It's recommended you use some development tools:
- [**LocalStack**](https://github.com/localstack/localstack)

### Stack CLI configuration
Run the command below to update the local Stack with the catalog that contains the OpenAPI plugin:
```bash
stk add stack https://github.com/stack-spot/crystal-typescript-api-stack
```

#### Template and plugin verification
Run the command below to list and verify that catalog was loaded locally.
**Plugin listing available locally:**
```bash
stk list plugin
```

**Output example:**
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

**Template listing available locally:**
```bash
stk list template
```

**Output example:**
```bash
Stack: crystal-typescript-api-stack
+----------------------+---------------------------------------------+------------------+-----------------+
| name                 | description                                 | types            | version(latest) |
+----------------------+---------------------------------------------+------------------+-----------------+
| base-app-ts-template | Base template to work with typescript stack | ['app-template'] | no release      |
|                      |                                             |                  |                 |
+----------------------+---------------------------------------------+------------------+-----------------+
```

### Install
The steps in this section show how to create and configure the plugin in the application.

**Step 1.** Copy and paste the URL below into your terminal:
```bash
stk create app meu-teste-app -t crystal-typescript-api-stack/base-app-ts-template
```

**Step 2.** Access created project:
```bash
cd meu-teste-app
```

**Step 3.** Catalog based plugin application:
```bash
stk apply plugin crystal-typescript-api-stack/app-typescript-openapi-plugin
```

### Inputs
Below are listed the plugin inputs.

The inputs needed to use the plugin are:

| Field                              | Type | Description                                                                                                           | Default Value  |
|:-----------------------------------|:-----|:----------------------------------------------------------------------------------------------------------------------|:---------------|
| *api_name*                         | text | Defines the name of the API, also used to link generated codes and code references.                                   | api-name       |
| *import_spec_file*                 | bool | Defines whether the user wants to import an OpenAPI specification file.                                               | True           |
| *import_spec_file_path*            | text | Defines the path to the specification file that will be imported. Note: only used if **import_spec_file** is **True** |                |
| *spec_file_name*                   | text | Defines the name of the OpenAPI specification file located in the /spec directory, by default it is spec-file-name.   | spec-file-name |
| *source_dir*                       | text | Sets the path, starting from the project root, of the generated OpenAPI lambda files, by default it is src.           | src            |
| *access_control_allow_origin*      | text | Defines the use of custom Access-Control-Allow-Origin of endpoints.                                                   | *              |
| *access_control_allow_headers*     | text | Defines the use of custom Access-Control-Allow-Headers of endpoints.                                                  | *              |
| *access_control_allow_methods*     | text | Defines the use of custom Access-Control-Allow-Methods of endpoints.                                                  | *              |
| *access_control_allow_credentials* | text | Defines the use of custom Access-Control-Allow-Credentials of endpoints.                                              | *              |

## Tutorial
After creating and applying the plugin, it is possible to deploy the generated _Lambda_ application.

### 1. CDK bootstrap
1. Runs the _CDK bootstrap_ to prepare the stack and generate the service stubs. 
```
cdk bootstrap --profile <your-aws-profile>
```

#### Problem related to S3 public access
If you have permissions problems related to S3 public access block configuration permissions on bootstrap you could add the option `--public-access-block-configuration false` to the bootstrap command as shown below:  
```
cdk bootstrap --profile <your-aws-profile> --public-access-block-configuration false
```
> Obs.: If use _npm run cdk bootstrap_ to use this option it is necessary to add `--` after the command (bootstrap):  
> ```
> npm run cdk bootstrap -- --public-access-block-configuration false
> ```

#### CDK Local
This plugin configures automatically (for DEV environment) the use of _CDK Local_  
To use LocalStack and do a local bootstrap, run the command below:
```
npm run local bootstrap
```

### 2. Alterar retorno do endpoint
Edit generated _usecase_ stub (`{{source_dir}}/post-hello/usecase.ts`) and implement the code to generate the expected response imported from `{{source_dir}}/api-models.ts` as shown below:  
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

### 3. Build, deploy e chamada da API
Run `npm run build`, `cdk deploy` and call API at the endpoint created with an appropriate payload.  
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

After OpenAPI Plugin has been applied, editing the file `{{spec_file_name}}.yaml` enables updating the generated service stubs based on this file.  

