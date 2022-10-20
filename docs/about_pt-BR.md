## Visao Geral
### Como Typescript OpenAPI Plugin funciona
Por meio das linhas de comando StackSpot, é possível aplicar o plugin em uma aplicação do tipo APP. 
Ao realizar a aplicação o template de _construct_ cdk é criado na aplicação, utilizando o componente `@stackspot/cdk-component-openapi-typescript`.  
Durante a aplicação do plugin é gerado o código Lambda baseado na especificação OpenAPI definida no arquivo `infra/spec/{{spec_file_name}}.yaml`.