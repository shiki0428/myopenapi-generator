SHELL=/bin/zsh


# set_up:

#orign-openapi-generator/modules/openapi-generator 以下のファイルを変更した際に最新化するために実行
origin_jar_create:
	@mvn package -DskipTests=true -f ./origin-openapi-generator/modules/openapi-generator/pom.xml
	@mv ./origin-openapi-generator/modules/openapi-generator/target/openapi-generator-6.4.0-SNAPSHOT.jar ./fastapi-openapi/tools/openapi-generator_origin.jar 

#orign-openapi-generator/modules/openapi-generator-cli 以下のファイルを変更した際に最新化するために実行
origin_cli_jar_create:
	@mvn package -DskipTests=true -f ./origin-openapi-generator/modules/openapi-generator-cli/pom.xml
	@mv ./origin-openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar ./fastapi-openapi/tools/openapi-generator-cli_origin.jar 

#openapi-custom-generator 以下のファイルを変更した際に最新化するために実行
custom_jar_create:
	@mvn package -DskipTests=true -f ./openapi-custom-generator/pom.xml
	@mv ./openapi-custom-generator/target/fastapi-custom-server-openapi-generator-1.0.0.jar ./fastapi-openapi/tools 


#上記　make コマンド実行後に作成されるjarファイルを実行することで自前のopenapi-generatorを実行することができる
custom_generate:
	@rm -rf ./fastapi-openapi/generate/
	@java -cp ./fastapi-openapi/tools/openapi-generator_origin.jar:./fastapi-openapi/tools/openapi-generator-cli_origin.jar:./fastapi-openapi/tools/fastapi-custom-server-openapi-generator-1.0.0.jar org.openapitools.codegen.OpenAPIGenerator generate -g fastapi-custom-server -i ./fastapi-openapi/api/openapi.yaml -o ./fastapi-openapi/generate/ > generate.log
 
 #上記　make コマンド実行後に作成されるjarファイルを実行することで自前のopenapi-generatorを実行することができる
custom_template_generate:
	@rm -rf ./fastapi-openapi/generate/
	@java -cp ./fastapi-openapi/tools/openapi-generator_origin.jar:./fastapi-openapi/tools/openapi-generator-cli_origin.jar:./fastapi-openapi/tools/fastapi-custom-server-openapi-generator-1.0.0.jar org.openapitools.codegen.OpenAPIGenerator generate -g fastapi-custom-server -i ./fastapi-openapi/api/openapi.yaml -o ./fastapi-openapi/generate/ -t ./fastapi-openapi/template/fastapi-custom-server/ > generate.log
 
#オープンソースの何も修正されていない状態のopenapi-generator
origin_generate:
	@openapi-generator generate -g python-fastapi -i ./fastapi-openapi/api/openapi.yaml -o ./fastapi-openapi/origin_generate/ > generate.log

#オープンソースの何も修正されていない状態のopenapi-generator
origin_template_generate:
	@openapi-generator generate -g python-fastapi -i ./fastapi-openapi/api/openapi.yaml -o ./fastapi-openapi/origin_generate/ -t ./fastapi-openapi/template/ > generate.log


#pathの追加
add_path:
	@cp fastapi-openapi/config/importpath.pth ./venv/lib/python3.9/site-packages/importpath.pth

run_server:
	@venv/bin/uvicorn main:app --reload


help:
	@grep "^[a-zA-Z_\-]*:" Makefile | grep -v "grep" | sed -e 's/^/make /' 

#DBからスキーマ情報を取得する
sql_codegen:
	@venv/bin/sqlacodegen postgresql://user:user@localhost:5432/postgres --outfile ./fastapi-openapi/common/database/models.py 

#migrateの作成
alembic_revision:
	@venv/bin/alembic revision --autogenerate -m "tag table add is_active"

#更新を最新化
alembic_upgrade:
	@venv/bin/alembic upgrade head   
