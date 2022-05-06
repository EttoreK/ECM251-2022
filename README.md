# ECM251 - Utilizando Git

- Ordem para criar um repositório:
- Inicializar o repositório:
```bash
git init
```

- Para novos terminais
```bash
git clone "link do repositório"
```

- Para terminais já configurados
```bash
git pull
```

- Em primeiro lugar, configurar quem é o usuário (***nome***) e qual seu ***e-mail***.

```bash
git config --global user.name "nomeusuario"
git config --global user.email email@email.com
```

- Adicionar os arquivos com:
```bash
git add .
```
- Comitar (salvar) os arquivos:
```bash
git commit -m  "mensagem"
```

- Enciar as alterações para a nuvem:
```bash
git push
```

- Criar repositórios por linha de Comando
```bash 
git branch -M main
git remote add origin "https://github.com/nomeusuario/nomerepositorio.git"
git push -u origin main
```

- Verificar Status
```bash
git status
```
