import glob
import os
import yaml
import shutil

with open(os.path.join(os.getcwd(), 'services.yml')) as file:
    config = yaml.safe_load(file)
    services = config['services']

    for service_name, service_conf in services.items():
        src_path = os.path.join(os.getcwd(), service_conf['src'])
        if not os.path.isdir(src_path):
            raise Exception(
                "%s component is missing from the file structure" % service_name)

        build_type = service_conf['build']

        print(f"Building {service_name}...")

        if build_type == 'python':

            setup_file = os.path.join(src_path, 'setup.py')

            if not os.path.isfile(setup_file):
                raise Exception('%s has invalid configuration set. %s is not present in the service\'s source directory' % (
                    service_name, 'setup.py'))

            os.system(f"cd {src_path} && python {setup_file} bdist_wheel")

            dist_match = glob.glob(os.path.join(src_path, 'dist', '*.whl'))

            if len(dist_match) == 0:
                raise Exception("%s failed building process" % service_name)

            dist_file_name = f'{service_name}.whl'

            dist_path = os.path.join(
                os.getcwd(), service_conf['dist'])

            if not os.path.isdir(dist_path):
                os.mkdir(dist_path)

            os.rename(dist_match[0], os.path.join(dist_path, dist_file_name))

        elif build_type == 'copy':
            src_path = os.path.join(os.getcwd(), service_conf['src'])
            dist_path = os.path.join(os.getcwd(), service_conf['dist'])

            if os.path.isdir(dist_path):
                shutil.rmtree(dist_path)

            shutil.copytree(src_path, dist_path)

        elif build_type == 'vue':
            os.system("cd %s && npm run build" % service_name)

            if not os.path.isdir(os.path.join(src_path, 'dist')):
                raise Exception("%s building process failed" % service_name)

            build_path = os.path.join(src_path, 'dist')
            dist_path = os.path.join(os.getcwd(), service_conf['dist'])

            if os.path.isdir(dist_path):
                shutil.rmtree(dist_path)

            shutil.copytree(build_path, dist_path)

        print("Finished building %s" % service_name)
