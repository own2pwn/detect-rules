RULES = {
    "jQuery": {
        "regex": "jQuery v([\\d.]+)",
        "alias": "jquery",
        "type": "software"
    },
    "Phusion Passenger": {
        "regex": "Phusion Passenger(?: \\([a-zA-Z_/]+\\))? ([\\d.]+)",
        "alias": "cpe:/a:phusion:passenger",
        "type": "cpe"
    },
    "IBM WebSphere Application Server": {
        "regex": "WebSphere Application Server/([\\d.]+)",
        "alias": "WebSphere",
        "type": "software"
    },
    "jQuery UI Core": {
        "regex": "jQuery UI Core ([\\d.]+)",
        "alias": "jquery-ui",
        "type": "software"
    },
    "mod_perl": {
        "regex": "mod_perl/([\\d.]+)",
        "alias": "cpe:/a:apache:mod_perl",
        "type": "cpe"
    },
    "Undertow": {
        "regex": "X-Powered-By: Undertow/([\\d.]+)",
        "alias": "cpe:/a:redhat:undertow",
        "type": "cpe"
    },
    "Google Web Toolkit (GWT)": {
        "regex": "\\$gwt_version\\s?=\\s?\"([\\d.]+)\"",
        "alias": "cpe:/a:google:web_toolkit",
        "type": "cpe"
    },
    "IBM HTTP Server": {
        "regex": "IBM_HTTP_Server/([\\d.]+)",
        "alias": "IBM HTTP Server",
        "type": "software"
    },
    "Perl": {
        "regex": "Perl/v([\\d.]+)",
        "alias": "Perl",
        "type": "software"
    },
    "CKEditor": {
        "regex": "CKEDITOR.*version:\"([\\d.]+)\"",
        "alias": "cpe:/a:ckeditor:ckeditor",
        "type": "cpe"
    },
    "IBM TeaLeaf": {
        "regex": "X-TeaLeaf-UIEventCapture-Version: ([\\d.]+)",
        "alias": "cpe:/a:ibm:tealeaf_consumer_experience",
        "type": "cpe"
    },
    "Oracle Java": {
        "regex": "Oracle Corporation ([\\d\\._])+",
        "alias": "Oracle Java",
        "type": "software"
    },
    "Handlebars.js": {
        "regex": "Handlebars\\.VERSION\\s*=\\s*[\"']([\\w.]+)[\"']",
        "alias": "Handlebars",
        "type": "software"
    },
    "Microsoft IIS": {
        "regex": "Microsoft-IIS/([\\d.]+)",
        "alias": "cpe:/a:microsoft:iis",
        "type": "cpe"
    },
    "Apache Tomcat": {
        "regex": "Apache Tomcat/([\\d.]+)",
        "alias": "cpe:/a:apache:tomcat",
        "type": "cpe"
    },
    "Apache Cocoon": {
        "regex": "X-Cocoon-Version: ([\\d.]+)",
        "alias": "cpe:/a:apache:cocoon",
        "type": "cpe"
    },
    "ASP.Net MVC Framework": {
        "regex": "X-AspNetMvc-Version: ([\\d.]+)",
        "alias": "cpe:/a:microsoft:asp.net",
        "type": "cpe"
    },
    "Microsoft .Net Framework": {
        "regex": "Microsoft \\.NET Framework ([\\d.]+)",
        "alias": "cpe:/a:microsoft:.net_framework",
        "type": "cpe"
    },
    "Microsoft SharePoint": {
        "regex": "MicrosoftSharePointTeamServices: ([\\d.]+)",
        "alias": "cpe:/a:microsoft:sharepoint",
        "type": "cpe"
    },
    "WildFly": {
        "regex": "Server: WildFly/([\\d.]+)",
        "alias": "cpe:/a:redhat:jboss_wildfly_application_server",
        "type": "cpe"
    },
    "JBoss Enterprise Application Platform": {
        "regex": "JBoss-EAP/([\\d.]+)",
        "alias": "cpe:/a:redhat:jboss_enterprise_application_platform",
        "type": "cpe"
    },
    "Oracle iPlanet": {
        "regex": "Sun-Java-System-Web-Server/([\\d.]+.*)",
        "alias": "cpe:/a:oracle:iplanet_web_server",
        "type": "cpe"
    },
    "lighttpd": {
        "regex": "lighttpd/([\\d.]+)",
        "alias": "cpe:/a:lighttpd:lighttpd",
        "type": "cpe"
    },
    "mod_ssl": {
        "regex": "mod_ssl/([\\d.]+)",
        "alias": "cpe:/a:modssl:mod_ssl",
        "type": "cpe"
    },
    "AngularJS": {
        "regex": "http://errors\\.angularjs\\.org/([\\d.]+)/",
        "alias": "Angular",
        "type": "software"
    },
    "Igor Sysoev nginx": {
        "regex": "nginx/([\\d.]+)",
        "alias": "cpe:/a:igor_sysoev:nginx",
        "type": "cpe"
    },
    "nginx": {
        "regex": "nginx/([\\d.]+)",
        "alias": "cpe:/a:nginx:nginx",
        "type": "cpe"
    },
    "OpenCms": {
        "regex": "OpenCms/([\\d.]+)",
        "alias": "cpe:/a:alkacon:opencms",
        "type": "cpe"
    },
    "jQuery UI": {
        "regex": "jQuery UI ([\\d.]+)",
        "alias": "jquery-ui",
        "type": "software"
    },
    "Ember": {
        "regex": "Ember\\.VERSION\\s*=\\s*[\"']([\\w.]+)[\"']",
        "alias": "cpe:/a:emberjs:ember.js",
        "type": "cpe"
    },
    "Tornado Server": {
        "regex": "TornadoServer/([\\d.]+)",
        "alias": "cpe:/a:tornadoweb:tornado",
        "type": "cpe"
    },
    "Nexpose": {
        "regex": "NSC/([\\d.]+) \\(JVM\\)",
        "alias": "cpe:/a:rapid7:nexpose",
        "type": "cpe"
    },
    "Outlook Web Access": {
        "regex": "X-OWA-Version: ([\\d.]+)",
        "alias": "cpe:/a:microsoft:outlook_web_access",
        "type": "cpe"
    },
    "Java Server Faces": {
        "regex": "JSF/([\\d.]+)",
        "alias": "cpe:/a:oracle:mojarra",
        "type": "cpe"
    },
    "Ruby": {
        "regex": "Ruby/([\\d.]+(?:/\\d{4}-\\d{2}-\\d{2})?)",
        "alias": "Ruby",
        "type": "software"
    },
    "Oracle OpenSSO": {
        "regex": "Oracle OpenSSO ([\\d.]+.*)",
        "alias": "cpe:/a:oracle:opensso",
        "type": "cpe"
    },
    "Joomla!": {
        "regex": "Joomla! ([\\d.]+)",
        "alias": "Joomla",
        "type": "software"
    },
    "Apache Coyote (Tomcat)": {
        "regex": "Apache-Coyote/([\\d.]+)",
        "alias": "cpe:/a:apache:tomcat",
        "type": "cpe"
    },
    "Jetty": {
        "regex": "Jetty\\([v\\d.]+\\)",
        "alias": "cpe:/a:mortbay:jetty",
        "type": "cpe"
    },
    "Apache": {
        "regex": "Apache/([\\d.]+(?: \\([ \\w]+\\))?)",
        "alias": "httpd",
        "type": "software"
    },
    "Oracle-Application-Server": {
        "regex": "Oracle-Application-Server-([\\d.]+.*)",
        "alias": "cpe:/a:oracle:application_server",
        "type": "cpe"
    },
    "PHP": {
        "regex": "PHP/([\\d.]+)",
        "alias": "cpe:/a:php:php",
        "type": "cpe"
    },
    "OpenSSL": {
        "regex": "OpenSSL/([a-z\\d.]+(-fips)?)",
        "alias": "OpenSSL",
        "type": "software"
    },
    "ASP.Net": {
        "regex": "X-AspNet-Version: ([\\d.]+)",
        "alias": "cpe:/a:microsoft:asp.net",
        "type": "cpe"
    },
    "Microsoft CRM": {
        "regex": "var APPLICATION_FULL_VERSION = '([\\d.]+)';",
        "alias": "cpe:/a:microsoft:business_solutions_crm",
        "type": "cpe"
    },
    "JBoss": {
        "regex": "JBPAPP_([\\d_]+(?:GA)?)",
        "alias": "cpe:/a:redhat:jboss",
        "type": "cpe"
    },
    "jQuery JavaScript Library": {
        "regex": "jQuery JavaScript Library v([\\d.]+)",
        "alias": "jquery",
        "type": "software"
    },
    "Wordpress": {
        "regex": 'name="generator" content="WordPress ([\\d.]+)"',
        "alias": "wordpress",
        "type": "software"
    },
    "Java": {
        "regex": "java\\/([\\d\\.\\_]+)",
        "alias": "cpe:/a:oracle:jre",
        "type": "cpe",
    },
    "GlassFish Server": {
        "regex": "GlassFish Server Open Source Edition ([\\d\\.]+)",
        "alias": "cpe:/a:oracle:glassfish_server",
        "type": "cpe",
    },
    "Oracle Weblogic": {
        "regex": "WebLogic (:?Server )?([\\d\\.]+)",
        "alias": "cpe:/a:oracle:weblogic_server",
        "type": "cpe",
    },
    "Oracle Application Server Containers for J2EE 10g": {
        "regex": "Oracle Application Server Containers for J2EE 10g \\(([\\d\\.]+)\\)",
        "alias": "cpe:/a:oracle:application_server",
        "type": "cpe",
    },
    "Oracle Application Server 10g": {
        "regex": "Oracle.Application.Server.10g\\/([\\d\\.]+)",
        "alias": "cpe:/a:oracle:application_server",
        "type": "cpe",
    },
    "Oracle Application Server": {
        "regex": "Oracle Application Server\\/([\\d\\.]+)",
        "alias": "cpe:/a:oracle:application_server",
        "type": "cpe",
    },
    "Oracle9iA": {
        "regex": "Oracle9iAS\\/([\\d\\.]+)",
        "alias": "cpe:/a:oracle:application_server",
        "type": "cpe",
    },
    "Apache Traffic Server": {
        "regex": "Server:\\s*ATS/?([\\d.]+)",
        "alias": "cpe:/a:apache:traffic_server",
        "type": "cpe"
      },
    "JBoss Application Server": {
        "regex": "X-Powered-By:\\s*JBoss-([\\d.]+)",
        "alias": "cpe:/a:redhat:jboss_community_application_server",
        "type": "cpe"
      },
    "TwistedWeb": {
        "regex": "Server:\\s*TwistedWeb/([\\d.]+)",
        "alias": "cpe:/a:twistedmatrix:twistedweb",
        "type": "cpe"
      },
    "JavaServer Pages": {
        "regex": "X-Powered-By:\\s*JSP/([\\d.]+)",
        "alias": "JavaServer Pages",
        "type": "software"
      },
    "IBM HTTP Server, header detect": {
        "regex": "Server:\\s*IBM_HTTP_Server/([\\d.]+)",
        "alias": "cpe:/a:ibm:http_server",
        "type": "cpe"
      },
    "Joomla, header detect": {
        "regex": "X-Content-Encoded-By:\\s*Joomla! ([\\d.]+)",
        "alias": "joomla",
        "type": "software"
      },
    "Lua": {
        "regex": "X-Powered-By:\\s*\bLua ([\\d.]+)",
        "alias": "cpe:/a:lua:lua",
        "type": "cpe"
      },
    "AMPcms": {
        "regex": "X-AMP-Version:\\s*([\\d.]+)",
        "alias": "AMP CMS",
        "type": "software"
      },
    "GlassFish": {
        "regex": "Server:\\s*GlassFish Server Open Source Edition ?/?([\\d.]+)",
        "alias": "cpe:/a:oracle:glassfish_server",
        "type": "cpe"
      },
    "IIS": {
        "regex": "Server:\\s*IIS/([\\d.]+)",
        "alias": "cpe:/a:microsoft:iis",
        "type": "cpe"
      },
    "Artifactory Web Server": {
        "regex": "Server:\\s*Artifactory/([\\d.]+)",
        "alias": "cpe:/a:jfrog:artifactory",
        "type": "cpe"
      },
    "Kohana": {
        "regex": "X-Powered-By:\\s*Kohana Framework ([\\d.]+)",
        "alias": "Kohana",
        "type": "software"
    },
    "mod_ssl, server banner": {
        "regex": "Server:\\s*mod_ssl/([\\d.]+)",
        "alias": "cpe:/a:modssl:mod_ssl",
        "type": "cpe"
    },
    "Akka HTTP": {
        "regex": "Server:\\s*akka-http/([\\d.]+)",
        "alias": "Akka HTTP",
        "type": "software"
    },
    "Oracle Commerce": {
        "regex": "X-ATG-Version:\\s*ATGPlatform/([\\d.]+)",
        "alias": "cpe:/a:oracle:commerce_platform",
        "type": "cpe"
    },
    "WP Rocket": {
        "regex": "X-Powered-By:\\s*WP Rocket/([\\d.]+)",
        "alias": "WP Rocket",
        "type": "software"
    },
    "Perl Dancer, server banner": {
        "regex": "Server:\\s*Perl Dancer ([\\d.]+)",
        "alias": "cpe:/a:dancer:dancer",
        "type": "cpe"
    },
    "Perl Dancer, header banner": {
        "regex": "X-Powered-By:\\s*Perl Dancer ([\\d.]+)",
        "alias": "cpe:/a:dancer:dancer",
        "type": "cpe"
    },
    "FlexCMP, header banner": {
        "regex": "X-Powered-By:\\s*FlexCMP.+\\[v\\. ([\\d.]+)",
        "alias": "FlexCMP",
        "type": "software"
    },
    "FlexCMP": {
        "regex": "<!--[^>]+FlexCMP[^>v]+v\\. ([\\d.]+)",
        "alias": "FlexCMP",
        "type": "software"
    },
    "Atlassian FishEye": {
        "regex": "<title>Log in to FishEye and Crucible ([\\d.]+)</title>",
        "alias": "cpe:/a:atlassian:fisheye",
        "type": "cpe"
    },
    "Embedthis-http": {
        "regex": "Server:\\s*Embedthis-http/([\\d.]+)",
        "alias": "cpe:/a:embedthis:appweb",
        "type": "cpe"
    },
    "Doxygen": {
        "regex": "<!-- Generated by Doxygen ([\\d.]+)",
        "alias": "Doxygen",
        "type": "software"
    },
    "PHP, header banner": {
        "regex": "X-Powered-By:\\s*php/?([\\d.]+)",
        "alias": "cpe:/a:php:php",
        "type": "cpe"
    },
    "PHP, server banner": {
        "regex": "Server:\\s*php/?([\\d.]+)",
        "alias": "cpe:/a:php:php",
        "type": "cpe"
    },
    "JBoss Web": {
        "regex": "X-Powered-By:\\s*JBossWeb-([\\d.]+)",
        "alias": "cpe:/a:redhat:jboss_enterprise_web_server",
        "type": "cpe"
    },
    "SimpleHTTP": {
        "regex": "Server:\\s*SimpleHTTP/([\\d.]+)",
        "alias": "SimpleHTTP",
        "type": "software"
    },
    "IBM Tivoli Storage Manager": {
        "regex": "Server:\\s*TSM_HTTP/([\\d.]+)",
        "alias": "cpe:/a:ibm:tivoli_storage_manager",
        "type": "cpe"
    },
    "DirectAdmin": {
        "regex": "Server:\\s*DirectAdmin Daemon v([\\d.]+)",
        "alias": "cpe:/a:directadmin:directadmin",
        "type": "cpe"
    },
    "RAID HTTPServer": {
        "regex": "Server:\\s*RAID HTTPServer/([\\d.]+)",
        "alias": "RAID HTTPServer",
        "type": "software"
    },
    "Coppermine": {
        "regex": "<!--Coppermine Photo Gallery ([\\d.]+)",
        "alias": "cpe:/a:coppermine-gallery:coppermine_photo_gallery",
        "type": "cpe"
    },
    "Google PageSpeed": {
        "regex": "X-Mod-Pagespeed:\\s*([\\d.]+)",
        "alias": "cpe:/a:google:mod_pagespeed",
        "type": "cpe"
    },
    "Kibana": {
        "regex": "kbn-version:\\s*^([\\d.]+)$",
        "alias": "cpe:/a:elasticsearch:kibana",
        "type": "cpe"
    },
    "Motion-httpd": {
        "regex": "Server:\\s*Motion-httpd/([\\d.]+)",
        "alias": "Motion-httpd",
        "type": "software"
    },
    "Artifactory": {
        "regex": "<span class=\"version\">Artifactory Pro Power Pack ([\\d.]+)",
        "alias": "cpe:/a:jfrog:artifactory",
        "type": "cpe"
    },
    "Django": {
        "regex": "powered by <a[^>]+>Django ?([\\d.]+)",
        "alias": "cpe:/a:djangoproject:django",
        "type": "cpe"
    },
    "Apache, server banner": {
        "regex": "Server:\\s*Apache/([\\d.]+)",
        "alias": "httpd",
        "type": "software"
    },
    "Oracle HTTP Server": {
        "regex": "Server:\\s*Oracle-HTTP-Server/([\\d.]+)",
        "alias": "cpe:/a:oracle:http_server",
        "type": "cpe"
    },
    "Allegro RomPager": {
        "regex": "Server:\\s*Allegro-Software-RomPager/([\\d.]+)",
        "alias": "cpe:/a:allegrosoft:rompager",
        "type": "cpe"
    },
    "Schneider Web Server": {
        "regex": "Server:\\s*Schneider-WEB/V?([\\d.]+)",
        "alias": "Schneider Web Server",
        "type": "software"
    },
    "Cherokee": {
        "regex": "Server:\\s*Cherokee/([\\d.]+)",
        "alias": "cpe:/a:cherokee-project:cherokee",
        "type": "cpe"
    },
    "mini_httpd": {
        "regex": "Server:\\s*mini_httpd/([\\d.]+)",
        "alias": "cpe:/a:acme:mini_httpd",
        "type": "cpe"
    },
    "Chamilo, regex detect": {
        "regex": "\">Chamilo ([\\d.]+)</a>",
        "alias": "cpe:/a:chamilo:chamilo_lms",
        "type": "cpe"
    },
    "Chamilo, header banner": {
        "regex": "X-Powered-By:\\s*Chamilo ([\\d.]+)",
        "alias": "cpe:/a:chamilo:chamilo_lms",
        "type": "cpe"
    },
    "MediaTomb": {
        "regex": "Server:\\s*MediaTomb/([\\d.]+)",
        "alias": "MediaTomb",
        "type": "software"
    },
    "Microsoft HTTPAPI": {
        "regex": "Server:\\s*Microsoft-HTTPAPI/([\\d.]+)",
        "alias": "Microsoft HTTPAPI",
        "type": "software"
    },
    "W3 Total Cache": {
        "regex": "X-Powered-By:\\s*W3 Total Cache/([\\d.]+)",
        "alias": "cpe:/a:w3edge:total_cache",
        "type": "cpe"
    },
    "JC-HTTPD": {
        "regex": "Server:\\s*JC-HTTPD/([\\d.]+)",
        "alias": "JC-HTTPD",
        "type": "software"
    },
    "OpenSSL, server banner": {
        "regex": "Server:\\s*OpenSSL/([\\d.]+[a-z]?)",
        "alias": "OpenSSL",
        "type": "software"
    },
    "cPanel": {
        "regex": "Server:\\s*cpsrvd/([\\d.]+)",
        "alias": "cpe:/a:cpanel:cpanel",
        "type": "cpe"
    },
    "Winstone Servlet Container, server banner": {
        "regex": "Server:\\s*Winstone Servlet Container v?([\\d.]+)",
        "alias": "cpe:/a:jenkins:jenkins",
        "type": "cpe"
    },
    "Winstone Servlet Container, server banner 2": {
        "regex": "Server:\\s*Winstone Servlet Engine v?([\\d.]+)",
        "alias": "cpe:/a:jenkins:jenkins",
        "type": "cpe"
    },
    "Winstone Servlet Container, header banner": {
        "regex": "X-Powered-By:\\s*Winstone.([\\d.]+)",
        "alias": "cpe:/a:jenkins:jenkins",
        "type": "cpe"
    },
    "Adminer, regex 1": {
        "regex": "Adminer</a> <span class=\"version\">([\\d.]+)</span>",
        "alias": "Adminer",
        "type": "software"
    },
    "Adminer, regex 2": {
        "regex": "onclick=\"bodyClick\\(event\\);\" onload=\"verifyVersion\\('([\\d.]+)'\\);\">",
        "alias": "Adminer",
        "type": "software"
    },
    "Atlassian Confluence": {
        "regex": "Powered by <a href=[^>]+atlassian\\.com/software/confluence[^>]+>Atlassian Confluence</a> ([\\d.]+)",
        "alias": "cpe:/a:atlassian:confluence",
        "type": "cpe"
    },
    "lighttpd, server banner": {
        "regex": "Server:\\s*lighttpd/([\\d.]+)",
        "alias": "cpe:/a:lighttpd:lighttpd",
        "type": "cpe"
    },
    "CppCMS": {
        "regex": "X-Powered-By:\\s*CppCMS/([\\d.]+)",
        "alias": "CppCMS",
        "type": "software"
    },
    "CouchDB": {
        "regex": "Server:\\s*CouchDB/([\\d.]+)",
        "alias": "cpe:/a:apache:couchdb",
        "type": "cpe"
    },
    "SonarQubes": {
        "regex": "<link href=\"/css/sonar\\.css?v=([\\d.]+)",
        "alias": "SonarQubes",
        "type": "software"
    },
    "Rapid Logic": {
        "regex": "Server:\\s*Rapid Logic/([\\d.]+)",
        "alias": "Rapid Logic",
        "type": "software"
    },
    "Danneo CMS": {
        "regex": "X-Powered-By:\\s*CMS Danneo ([\\d.]+)",
        "alias": "cpe:/a:danneo:cms",
        "type": "cpe"
    },
    "mod_fastcgi": {
        "regex": "Server:\\s*mod_fastcgi/([\\d.]+)",
        "alias": "mod_fastcgi",
        "type": "software"
    },
    "AOLserver": {
        "regex": "Server:\\s*AOLserver/?([\\d.]+)",
        "alias": "cpe:/a:aol:aolserver",
        "type": "cpe"
    },
    "TornadoServer": {
        "regex": "Server:\\s*TornadoServer/([\\d.]+)",
        "alias": "cpe:/a:tornadoweb:tornado",
        "type": "cpe"
    },
    "Gogs": {
        "regex": "<div class=\"ui left\">\n\\s+\u00a9 \\d{4} Gogs Version: ([\\d.]+) Page:",
        "alias": "cpe:/a:gogits:gogs",
        "type": "cpe"
    },
    "phpMyAdmin": {
        "regex": " \\| phpMyAdmin ([\\d.]+)<\\/title>",
        "alias": "cpe:/a:phpmyadmin:phpmyadmin",
        "type": "cpe"
    },
    "Moxa": {
        "regex": "Server:\\s*MoxaHttp/([\\d.]+)",
        "alias": "cpe:/h:moxa",
        "type": "cpe"
    },
    "Hiawatha": {
        "regex": "Server:\\s*Hiawatha v([\\d.]+)",
        "alias": "Hiawatha",
        "type": "software"
    },
    "eDevice SmartStack": {
        "regex": "Server:\\s*eDevice SmartStack ?/?([\\d.]+)",
        "alias": "eDevice SmartStack",
        "type": "software"
    },
    "Perl, server banner": {
        "regex": "Server:\\s*\bPerl\b ?/?v?([\\d.]+)",
        "alias": "Perl",
        "type": "software"
    },
    "HP Compact Server": {
        "regex": "Server:\\s*HP_Compact_Server/([\\d.]+)",
        "alias": "HP Compact Server",
        "type": "software"
    },
    "HP iLO": {
        "regex": "Server:\\s*HP-iLO-Server/([\\d.]+)",
        "alias": "cpe:/o:hp:integrated_lights-out",
        "type": "cpe"
    },
    "Xitami": {
        "regex": "Server:\\s*Xitami/([\\d.]+)",
        "alias": "cpe:/a:imatix:xitami",
        "type": "cpe"
    },
    "Happy ICS Server": {
        "regex": "Server:\\s*Happy ICS Server/([\\d.]+)",
        "alias": "Happy ICS",
        "type": "software"
    },
    "Apache Tomcat, header banner": {
        "regex": "X-Powered-By:\\s*\bTomcat\b-([\\d.]+)",
        "alias": "cpe:/a:apache:tomcat",
        "type": "cpe"
    },
    "Decorum": {
        "regex": "Server:\\s*DECORUM/([\\d.]+)",
        "alias": "Decorum",
        "type": "software"
    },
    "thttpd": {
        "regex": "Server:\\s*\bthttpd/([\\d.]+)",
        "alias": "cpe:/a:acme_labs:thttpd",
        "type": "cpe"
    },
    "Yaws": {
        "regex": "Server:\\s*Yaws ([\\d.]+)",
        "alias": "cpe:/a:yaws:yaws",
        "type": "cpe"
    },
    "mod_wsgi, server banner": {
        "regex": "Server:\\s*mod_wsgi/([\\d.]+)",
        "alias": "cpe:/a:modwsgi:mod_wsgi",
        "type": "cpe"
    },
    "mod_wsgi, header banner": {
        "regex": "X-Powered-By:\\s*mod_wsgi/([\\d.]+)",
        "alias": "cpe:/a:modwsgi:mod_wsgi",
        "type": "cpe"
    },
    "MochiWeb": {
        "regex": "Server:\\s*MochiWeb/([\\d.]+)",
        "alias": "cpe:/a:mochiweb_project:mochiweb",
        "type": "cpe"
    },
    "CenteHTTPd": {
        "regex": "Server:\\s*CenteHTTPd/([\\d.]+)",
        "alias": "CenteHTTPd",
        "type": "software"
    },
    "Outlook Web App": {
        "regex": "<link\\s[^>]*href=\"[^\"]*?([\\d.]+)/themes/resources/owafont\\.css",
        "alias": "OWA",
        "type": "software"
    },
    "YUI Doc": {
        "regex": "<html[^>]* yuilibrary\\.com/rdf/([\\d.]+)/yui\\.rdf|<body[^>]+class=\"yui3-skin-sam",
        "alias": "YUI Doc",
        "type": "software"
    },
    "gitweb": {
        "regex": "<!-- git web interface version ([\\d.]+)",
        "alias": "gitweb",
        "type": "software"
    },
    "EmbedThis Appweb": {
        "regex": "Server:\\s*Mbedthis-Appweb/([\\d.]+)",
        "alias": "cpe:/a:embedthis:appweb",
        "type": "cpe"
    },
    "GitPHP": {
        "regex": "<!-- gitphp web interface ([\\d.]+)",
        "alias": "GitPHP",
        "type": "software"
    },
    "gunicorn": {
        "regex": "Server:\\s*gunicorn/([\\d.]+)",
        "alias": "gunicorn",
        "type": "software"
    },
    "mod_dav": {
        "regex": "Server:\\s*\bmod_DAV\b/([\\d.]+)",
        "alias": "mod_dav",
        "type": "software"
    },
    "Intel Active Management Technology": {
        "regex": "Server:\\s*Intel\\(R\\) Active Management Technology ([\\d.]+)",
        "alias": "cpe:/o:intel:active_management_technology_firmware",
        "type": "cpe"
    },
    "Drupal": {
        "regex": "X-Generator:\\s*Drupal\\s([\\d.]+)",
        "alias": "Drupal",
        "type": "software"
    },

    "gitlist": {
        "regex": "<p>Powered by <a[^>]+>GitList ([\\d.]+)",
        "alias": "gitlist",
        "type": "software"
    },
    "HHVM": {
        "regex": "X-Powered-By:\\s*HHVM/?([\\d.]+)",
        "alias": "cpe:/a:facebook:hhvm",
        "type": "cpe"
    },
    "wpCache": {
        "regex": "X-Powered-By:\\s*wpCache/([\\d.]+)",
        "alias": "wpCache",
        "type": "software"
    },
    "FreeBSD": {
        "regex": "Server:\\s*FreeBSD ([\\d.]+)",
        "alias": "cpe:/o:freebsd:freebsd",
        "type": "cpe"
    },
    "Banshee": {
        "regex": "Built upon the <a href=\"[^>]+banshee-php\\.org/\">[a-z]+</a>v([\\d.]+)",
        "alias": "cpe:/a:banshee-project:banshee",
        "type": "cpe"
    },
    "mod_rack, server banner": {
        "regex": "Server:\\s*mod_rack/([\\d.]+)",
        "alias": "cpe:/a:apache:mod_rack",
        "type": "cpe"
    },
    "mod_rack, header banner": {
        "regex": "X-Powered-By:\\s*mod_rack/([\\d.]+)",
        "alias": "cpe:/a:apache:mod_rack",
        "type": "cpe"
    },
    "mod_rails, server banner": {
        "regex": "Server:\\s*mod_rails/([\\d.]+)",
        "alias": "cpe:/a:apache:mod_rails",
        "type": "cpe"
    },
    "mod_rails, header banner": {
        "regex": "X-Powered-By:\\s*mod_rails/([\\d.]+)",
        "alias": "cpe:/a:apache:mod_rails",
        "type": "cpe"
    },
    "mod_python": {
        "regex": "Server:\\s*mod_python/([\\d.]+)",
        "alias": "cpe:/a:apache:mod_python",
        "type": "cpe"
    },
    "JavaServer Faces": {
        "regex": "X-Powered-By:\\s*JSF/([\\d.]+)",
        "alias": "cpe:/a:oracle:mojarra",
        "type": "cpe"
    },
    "Indy": {
        "regex": "Server:\\s*Indy/([\\d.]+)",
        "alias": "Indy",
        "type": "software"
    },
    "Python": {
        "regex": "Server:\\s*Python/([\\d.]+)",
        "alias": "Python",
        "type": "software"
    },
    "Trac": {
        "regex": "Powered by <a href=\"[^\"]*\"><strong>Trac[ /]([\\d.]+)",
        "alias": "cpe:/a:edgewall_software:trac",
        "type": "cpe"
    },
    "OpenResty": {
        "regex": "Server:\\s*openresty/([\\d.]+)",
        "alias": "OpenResty",
        "type": "software"
    },
    "Liferay": {
        "regex": "Liferay-Portal:\\s*[a-z\\s]+([\\d.]+)",
        "alias": "cpe:/a:liferay:liferay_portal",
        "type": "cpe"
    },
    "Monkey HTTP Server": {
        "regex": "Server:\\s*Monkey/?([\\d.]+)",
        "alias": "cpe:/a:monkey-project:monkey_http_daemon",
        "type": "cpe"
    },
}
