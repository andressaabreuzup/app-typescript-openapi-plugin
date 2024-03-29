## Enabling JWT Security
- The _construct_ supports JWT tokens and this level of security can be enabled as [OpenAPI security scheme](https://swagger.io/specification/#security-scheme-object):
```yaml
components:
  securitySchemes:
    jwtAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```

- It is also possible to enable JWT token validation for all operations by setting security at the root of the OpenAPI specification or each operation as demonstrated below:

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

- Most _IDM_ providers expose the _JWKS_URI_ with their public keys to verify JWT token signatures. You need to configure the _construct_ as shown below to inform the _JWKS_URI_ that will be used to get the public keys:

```typescript
const api = new StackSpotOpenApiServices(this, 'StackSampleAPI', {
  specPath: 'spec/auction-api.yaml',
  jwksUri: 'https://some.idm.provider/auth/realms/some-realm/protocol/openid-connect/certs',
});
```

- If the project uses an _IDM_ that supports OpenID connection it is possible to get _JWKS_URI endpoint_ in [well-known endpoint](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfig) of OpenID connect provider.

- When enabled _JWT_ authorization controllers will extend the class `JWTAuthorizationController` and it is possible to override the method `authorizeResourceAccess` to make your own authorization logic. The _payload_ JWT token can be accessed through the property _protected_ `this.jwtTokenPayload`. Controllers already generated before JWT authorization will not be overwritten and must be changed by the user.

- With JWT authorization enabled, the Lambda API Gateway authorizer will be configured to validate the token.

- Authorization logic is not done by (lambda), only the authenticity and validity of the token are verified. You need to implement your own logic using _token claims_ in the controller operations or create a new class based on `JWTAuthorizationControler`, to use the base class, the controllers must implement authorization logic.

## References
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
