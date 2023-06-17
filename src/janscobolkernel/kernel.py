##!/usr/bin/env python
from ipykernel.kernelbase import Kernel
import pexpect, os, shutil

workingdir = "/tmp/cobolkernel/"

class janscobolkernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.12.0'
    language = 'cobol'
    language_version = '3.1.2'
    language_info = {
        'name': 'cobol',
        'mimetype': 'application/cobol',
        'file_extension': '.cob',
    }
    banner = "COBOL kernel"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            if os.path.exists(workingdir):
                shutil.rmtree(workingdir)
            os.mkdir(workingdir)
            os.chdir(workingdir)
            with open(workingdir + "proj.cob", "w") as f:
                    f.write(code)
            solution = pexpect.run('cobc -Ox -free ' + workingdir  + 'proj.cob').decode('UTF-8')
            if os.path.exists(workingdir + 'proj'):
                solution = pexpect.run(workingdir + 'proj').decode('UTF-8')
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

    def do_shutdown(self, restart):
        if os.path.exists(workingdir):
            shutil.rmtree(workingdir)
