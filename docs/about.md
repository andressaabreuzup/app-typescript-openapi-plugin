## Visão Geral
### **Funcionamento do Typescript OpenAPI Plugin**  
Por meio das linhas de comando da StackSpot (STK CLI) é possível aplicar o plugin em uma aplicação do tipo **APP**.

Ao aplicar o Template de **_construct_**, o **cdk** é criado na aplicação, utilizando o componente **`@stackspot/cdk-component-openapi-typescript`**.  

Durante a aplicação do Plugin, um código Lambda é gerado baseado na especificação **OpenAPI**, definida no arquivo **`infra/spec/{{spec_file_name}}.yaml`**. 