## **Habilitando a Segurança JWT**
O Template **_construct_** suporta tokens **JWT** e este nível de segurança pode ser habilitado conforme a especificação do [**OpenAPI security scheme**](https://swagger.io/specification/#security-scheme-object) abaixo:  

```yaml
components:
  securitySchemes:
    jwtAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

Também é possível habilitar a validação de token JWT para todas as operações, definindo a segurança na raiz da especificação OpenAPI ou em cada operação. Confira o exemplo abaixo:  

```yaml
# root level
security:
  - jwtAuth: []
paths:
  /auctions/{id}:
    parameters:
      - $ref: '#/components/parameters/AuctionId'
      - $ref: '#/components/parameters/Authorization'
    get:
      operationId: get-auction
      description: Get auction data by id
      # operation level
      security:
        - jwtAuth: []
      tags:
        - Auction services
      responses:
        '200':
          description: Auction returned successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Auction'
        '404':
          description: Auction not found
```

A maioria dos fornecedores **_IDM_** expõem a **_JWKS_URI_** com as próprias chaves públicas para verificar as assinaturas de token JWT. 

> É preciso configurar o **_construct_**
para informar _JWKS_URI_ que será usada para pegar as chaves públicas. Confira o exemplo abaixo:  

```typescript
const api = new StackSpotOpenApiServices(this, 'StackSampleAPI', {
  specPath: 'spec/auction-api.yaml',
  jwksUri: 'https://some.idm.provider/auth/realms/some-realm/protocol/openid-connect/certs',
});
```

Se o projeto utilizar um **_IDM_** que suporta conexão OpenID, é possível pegar _JWKS_URI endpoint_ em [well-known endpoint](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfig) 

- Quando a autorização _JWT_ é habilitada, os `controllers` extendem a classe `JWTAuthorizationController` e possibilitam sobrescrever o método `authorizeResourceAccess` para fazer uma lógica própria de autorização. 

O token JWT do `_payload_` pode ser acessado por meio da propriedade **_protected_ `this.jwtTokenPayload`**. 
Os controllers já gerados antes da autorização JWT não serão sobrescritos e devem ser alterados pelo usuário.

- Com a autorização JWT habilitada, o autorizador **`Lambda API Gateway`** será configurado para validar o token.

> A lógica de autorização não é feita pela Lambda, somente a autenticidade e validade do token são verificadas. Por isso, é preciso implementar a própria lógica utilizando _token claims_ nas operações dos controllers ou criar uma nova classe baseada em `JWTAuthorizationControler` para utilizar a classe base. Os controllers devem implementar a lógica de autorização.

## Referências
### CDK

- <https://docs.aws.amazon.com/cdk/latest/guide/home.html> - CDK Developer guide
- <https://docs.aws.amazon.com/cdk/api/latest/docs/aws-apigateway-readme.html> - CDK Amazon API Gateway Construct Library
- <https://aws.github.io/jsii/user-guides/lib-author/> - jsii library author guide
- <https://cdk-advanced.workshop.aws/> - CDK advanced workshop
- <https://docs.aws.amazon.com/cdk/latest/guide/videos.html> - CDK Videos

### API Gateway

- <https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html> - API Gateway developer guide
- <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-validation-set-up.html#api-gateway-request-validation-setup-importing-swagger> - How to setup API Gateway validation with OpenAPI extensions
- <https://stackoverflow.com/questions/47953570/get-detailed-error-messages-from-aws-api-gateway-request-validator> - How to get detailed body request validation messages in API Gateway

### OpenAPI

- <https://swagger.io/specification/> - OpenAPI 3.0 specification
- <https://stoplight.io/studio/> - StopLight Studio for visual specification editor and other cool features
