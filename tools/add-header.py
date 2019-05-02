# Licensed under the Apache License, Version 2.0 (the "License"). You may not
# use this file except in compliance with the License. A copy of the License is
# located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.


from argparse import ArgumentParser
import fnmatch
import os

class App:

    COMMENT_HEADER = """
# Licensed under the Apache License, Version 2.0 (the "License"). You may not
# use this file except in compliance with the License. A copy of the License is
# located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

"""
    def __init__(self):
        pass   

    def __call__(self):
        self.main()

    def addHeaderToFile(self, path):
        fileReader = open(path, "r")
        content = fileReader.readlines()
        # ignore empty files test if the header already exists
        # and add content accordingly
        if len(content) > 0 and type(content) is list:
            commentLines = App.COMMENT_HEADER.split("\n")
            for i in range(len(commentLines)):
                if commentLines[i]+"\n" != content[i]:
                    content.insert(i, commentLines[i]+"\n")

        fileReader.close()
        fileWriter = open(path, "w")
        fileWriter.seek(0)
        for line in content:
            if line.find('\n') ==  -1
                line += '\n'
            fileWriter.write(line)
        fileWriter.close()

    def setupParser(self):
        parser = ArgumentParser()
        parser.add_argument("--src-root", "-src",
            help="Source directory to discover files", 
            type=str, default=None, 
            required=True,
            dest="root")
        parser.add_argument("--file-masks","-ext", 
            help="File Masks to determine whether it's a source file",
            nargs="+",
            required = True,
            dest="patterns")
        return parser



    def discoverFiles(self, root, patterns):
        if not os.access(root, os.R_OK):
            raise ValueError("Can't read root {}".format(root))
        walker = os.walk(root)
        discoveredFiles = list()
        for root, dirs, files in walker:
            for pattern in patterns:
                sublist = fnmatch.filter(files, pattern)
                for i in range(0, len(sublist)):
                    sublist[i] = os.path.join(root, sublist[i])
                discoveredFiles += sublist
        return discoveredFiles

    def main(self):
        parser = self.setupParser()
        args = parser.parse_args()
        discoveredFiles = self.discoverFiles(args.root, args.patterns)
        map(self.addHeaderToFile, discoveredFiles)

if __name__ == "__main__":
    app = App()
    app()

