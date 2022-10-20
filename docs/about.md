## Overview
### How Typescript OpenAPI Plugin works
Through the StackSpot command lines, it is possible to apply the plugin in an APP type application.
When executing the application, the _construct_ cdk template is created in the application, using the component `@stackspot/cdk-component-openapi-typescript`.  
During the application of the plugin, the Lambda code is generated based on the OpenAPI specification defined in the file `infra/spec/{{spec_file_name}}.yaml`.
