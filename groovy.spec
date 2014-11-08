
Name:           groovy
Version:        2.3.7
Release:        0
Summary:        Dynamic language for the Java Platform

Group:          Development/Languages
# Some of the files are licensed under BSD and CPL terms, but the CPL has been superceded
# by the EPL. We include copies of both for completeness.
# groovyConsole uses CC-BY licensed icons
# (see: subprojects/groovy-console/target/tmp/groovydoc/groovy/ui/icons/credits.txt)
License:        ASL 2.0 and BSD and EPL and Public Domain and CC-BY
URL:            http://groovy.codehaus.org/
#Source0:        http://dist.groovy.codehaus.org/distributions/%{name}-src-%{version}.zip
Source0:        http://dl.bintray.com/groovy/maven/groovy-binary-%{version}.zip
BuildArch:      noarch

BuildRequires:  unzip
Requires:  jdk
%define __jar_repack %{nil}


%description
Groovy is an agile and dynamic language for the Java Virtual Machine,
built upon Java with features inspired by languages like Python, Ruby and
Smalltalk.  It seamlessly integrates with all existing Java objects and
libraries and compiles straight to Java bytecode so you can use it anywhere
you can use Java.


%prep
wget http://dl.bintray.com/groovy/maven/groovy-binary-%{version}.zip -O $RPM_SOURCE_DIR/groovy-binary-%{version}.zip
rm -rf %{buildroot}

%build


%install
mkdir -p %{buildroot}/opt
unzip $RPM_SOURCE_DIR/groovy-binary-%{version}.zip -d %{buildroot}/opt
rm -f %{buildroot}/opt/groovy-%{version}/bin/*.bat
chmod 755 %{buildroot}/opt/groovy-%{version}/bin/*

%post
ln -s /opt/groovy-%{version} /opt/groovy

update-alternatives --install /usr/bin/grape grape /opt/groovy-%{version}/bin/grape 2
update-alternatives --set grape /opt/groovy-%{version}/bin/grape
update-alternatives --install /usr/bin/groovy groovy /opt/groovy-%{version}/bin/groovy 2
update-alternatives --set groovy /opt/groovy-%{version}/bin/groovy
update-alternatives --install /usr/bin/groovyc groovyc /opt/groovy-%{version}/bin/groovyc 2
update-alternatives --set groovyc /opt/groovy-%{version}/bin/groovyc
update-alternatives --install /usr/bin/groovyConsole groovyConsole /opt/groovy-%{version}/bin/groovyConsole 2
update-alternatives --set groovyConsole /opt/groovy-%{version}/bin/groovyConsole
update-alternatives --install /usr/bin/groovydoc groovydoc /opt/groovy-%{version}/bin/groovydoc 2
update-alternatives --set groovydoc /opt/groovy-%{version}/bin/groovydoc
update-alternatives --install /usr/bin/groovysh groovysh /opt/groovy-%{version}/bin/groovysh 2
update-alternatives --set groovysh /opt/groovy-%{version}/bin/groovysh
update-alternatives --install /usr/bin/java2groovy java2groovy /opt/groovy-%{version}/bin/java2groovy 2
update-alternatives --set java2groovy /opt/groovy-%{version}/bin/java2groovy
update-alternatives --install /usr/bin/startGroovy startGroovy /opt/groovy-%{version}/bin/startGroovy 2
update-alternatives --set startGroovy /opt/groovy-%{version}/bin/startGroovy

%files
%defattr(-,root,root,-)
/opt/groovy-%{version}/*

%changelog
* Fri Nov 07 2014 Bear Wadleigh <bearlinux@gmail.com> - 2.3.7
* Fri Aug 08 2014 Bear Wadleigh <bwadleigh@glynlyon.com> - 2.3.6
- Initial try
