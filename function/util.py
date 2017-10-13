# coding: utf-8

import os
import re
import shutil
import subprocess
import zipfile

#
# # 压缩提取出来的文件
# def zipapp(app, pkgsdir):
#     pkgsdir = pkgsdir
#     app = app
#     # apps = [app for app in os.listdir(pkgsdir)
#     #         if os.path.isdir(os.path.join(pkgsdir, app))]
#     with open(pkgsdir + "/%s-lists.txt" % app, 'w') as f:
#         appdir = os.path.join(pkgsdir, app)
#         f.write('[' + app + ']' + '\n')
#         print pkgsdir + '/' + app + '.zip'
#         zip = zipfile.ZipFile(pkgsdir + '/' + app + '.zip', 'w')
#         for root, subroot, files in os.walk(appdir):
#             for file in files:
#                 full_path = os.path.join(root, file)
#                 relative_path = full_path.replace(appdir + '/', '')
#                 print full_path
#                 print relative_path
#                 f.write(relative_path + '\n')
#                 zip.write(full_path, relative_path)
#         zip.close()
#         shutil.rmtree(appdir)
#
#
# if __name__ == "__main__":
#
#     fl = set(fl)
#
#     # 抽取文件
#     src_pkg = providers[app]
#     zf = zipfile.ZipFile(src_pkg, 'r')
#     try:
#         zf.extractall(appdir, fl)
#     except Exception, e:
#         print e
#         os._exit(1)
#     zipapp(app=app, pkgsdir=pkgsdir)
#
#             prefix = os.path.split(fullpath)[0]
#             relative_path = prefix.replace('/data/web/%s' % app, '')
#             update_path = appdir + relative_path
#             print "update_path: ", update_path
#             if not os.path.exists(appdir + relative_path):
#                 os.makedirs(update_path)
#             shutil.copy2(fullpath, update_path)
#
#         '''
#         cmd = 'cp --parents %s ./pkgs/%s' % (fullpath, app)
#         cmd = ['cp', '--parents', fullpath, appdir+'/']
#         print cmd
#
#         p = subprocess.Popen(cmd, stderr=subprocess.PIPE)
#         out, err = p.communicate()
#         print err
#         '''
#     zipapp(app, pkgsdir=pkgsdir)



def update_web(app, filelist):
    # cmd = 'cp --parents %s ./pkgs/%s' % (fullpath, app)
    # cmd = ['cp', '--parents', fullpath, appdir+'/']
    cmd = ['ls /data/web/%s' % app]
    print cmd
    p = subprocess.Popen(cmd, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print err