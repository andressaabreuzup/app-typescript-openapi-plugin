## Use
This section shows how the plugin is used through the CLI, creating an application based on the template [**app-typescript-template**](https://github.com/stack-spot/app-typescript-template)  
After creating the application it is possible to apply the plugin **app-typescript-openapi-plugin**

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

Run the command below to import the Stack with the catalog that contains the OpenAPI plugin:
```bash
stk import stack https://github.com/stack-spot/crystal-typescript-api-stack
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
| *source_dir*                       | text | Define o caminho, a partir da raiz do projeto, dos arquivos OpenAPI lambda gerados, por padrão é src.                 | src            |
| *access_control_allow_origin*      | text | Sets the path, starting from the project root, of the generated OpenAPI lambda files, by default it is.               | *              |
| *access_control_allow_headers*     | text | Defines the use of custom Access-Control-Allow-Headers of endpoints                                                   | *              |
| *access_control_allow_methods*     | text | Defines the use of custom Access-Control-Allow-Methods of endpoints.                                                  | *              |
| *access_control_allow_credentials* | text | Defines the use of custom Access-Control-Allow-Credentials of endpoints.                                              | *              |
