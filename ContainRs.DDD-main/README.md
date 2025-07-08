# Preparando o ambiente
Stacks:

![technology Dotnet](https://img.shields.io/badge/techonolgy-Dotnet-orange)

## Criando o banco de dados a estrutura e dados iniciais do Identity

Abra o terminal, navegue para a pasta onde baixou o projeto e execute o comando abaixo:

```
dotnet ef database update --context IdentityDbContext --project .\src\ContainRs.Api\ContainRs.Api.csproj --startup-project .\src\ContainRs.Api\ContainRs.Api.csproj

```

This works:

```bash
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=Test123!" -p 1433:1433 --name sqlserver2 -d mcr.microsoft.com/mssql/server:2022-latest

dotnet ef database update --context IdentityDbContext --project ./src/ContainRs.Api/ContainRs.Api.csproj

```

## Criando o banco de dados a estrutura e dados iniciais de neg�cio

Abra o terminal, navegue para a pasta onde baixou o projeto e execute o comando abaixo:

```bash
dotnet ef database update --context AppDbContext --project .\src\ContainRs.Api\ContainRs.Api.csproj --startup-project .\src\ContainRs.Api\ContainRs.Api.csproj
```

This works:

```bash
dotnet ef database update --context AppDbContext --project ./src/ContainRs.Api/ContainRs.Api.csproj
```

## Rodando o projeto

O comando dever� criar o banco de dados e as tabelas necess�rias para o funcionamento do projeto.

```bash
dotnet run --project ./src/ContainRs.Api/ContainRs.Api.csproj
```

## Executar o utilities endpoint de card identifier

```bash
  curl -k -X POST https://localhost:7009/identify-card -H "Content-Type: application/json" -d '"4111111111111111"'
```
