Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices


- Project setup by reference Tutorial - https://www.youtube.com/watch?v=OLXkGB7krGo
- Live notes - https://bittersweet-mall-f00.notion.site/Code-along-build-an-ELT-Pipeline-in-1-Hour-dbt-Snowflake-Airflow-cffab118a21b40b8acd3d595a4db7c15#93439fcec8f64293a4577e7edc25e85f



SET UP SNOWFLAKE ROLE, WAREHOUSE, DATABASE AND SCHEMA - 

-- Select Super user role ----
use role accountadmin; -- This is in-built super user role in snowflake

--- Command to create warehouse, database and role ----
create warehouse if not exists dbt_wh with warehouse_size='x-small'; -- Create new warehouse small warehouse
create database if not exists  dbt_db; -- create new database
create role if not exists  dbt_role; -- create new role

---  Grant usage of warehouse and all database access to role ----
show grants on warehouse dbt_wh; -- Show all grants to user/role
grant usage on warehouse dbt_wh to role dbt_role; -- Grant warehouse usage privilege to dbt role
grant all on database dbt_db to role dbt_role; -- Grant full database priviledge to dbt_role

--- Assign role to user  ----
grant role dbt_role to user SEULIMISHRA; -- Grant dbt_role to user

--- Show all grants to role ---
show grants to role dbt_role; -- Show all grants to dbt_role

--- Selectc role ---
use role dbt_role;

-- Add dtb_schema inside dbt_database --
create schema dbt_db.dbt_schema;

--- Run follow command to drop the warehouse, database and role --
use role accountadmin;

--- Drop database, warehouse and role ---
drop database if exists dbt_db;
drop warehouse if exists dbt_wh;
drop role if exists dbt_role;



SET UP THE DBT PROJECT -

>> dbt init   (Run this command where you want to setup dbt project)

Profile yml file located in the following location. This contains  project name and snowflake connection creds along with db and schema.
Users/sovan.panda/.dbt/profiles.yml

Navigate to project root directory  and run following command to test the warehouse connection
>> dbt debug

Open dbt project in visual code and configure the the dbt_project.yaml file and packages:
>> code .

Run the following command to install packages in dbt project:
>> db deps
