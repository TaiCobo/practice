import os
from jinja2 import Environment, FileSystemLoader
import subprocess


if __name__ == '__main__':

    livedoor_home = "/Users/yanotaichi/Work/embulk/livedoor/"

    csv_path = livedoor_home + "csv/"
    yml_path = livedoor_home + "yml/"
    yml_temp_path = livedoor_home + "yml/temp/"
    env = Environment(loader=FileSystemLoader(yml_path, encoding='utf8'))
    tpl = env.get_template('templates/seed.yml')

    for file in os.listdir(csv_path):
        tablename = file[:-4]
        yml_contents = tpl.render({'tablename':tablename})

        with open(yml_path + "temp/temp_" + tablename + ".yml", mode='w') as f:
            f.write(yml_contents)

        cmd = "embulk guess " + yml_temp_path + "temp_" + tablename + ".yml -o " + yml_path + tablename + ".yml"
        subprocess.run(cmd.split())









