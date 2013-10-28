Name : kinfo
Version : 0.1.3
Release : 1 
Summary : Centos 6.X System Performance Check scripts
License : GPLv2+
Group : System Environment/Base
Source0 : kinfo.tar.gz
BuildRoot : ${_tmppath}/%{name}-${version}-%{release}-root

BuildArch : noarch
Packager : alinos <ickhyun@com2us.com>
Requires : dmidecode

%description
Cpu, Memory, Disk, Proccess info info check bash script
%prep
%setup
%build
%install
rm -rf %{buildroot}
%{__mkdir} -p $RPM_BUILD_ROOT/%{_bindir}
cp -a kinfo $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(-, root, root, 0755)
%{_bindir}/kinfo

%changelog
* Mon Sep 28 2013 alinos <alinos@alinos.net>
- rename kinfo
- cpu monitoring algorithm change (top command calculator)
- disk monitoring system change
- procinfo ARGS check item ADD
* Wed Aug 14 2013 alinos <alinos@alinos.net>
- 0.1.2
- BUG FIX cpu sequence change NICE <-> SYSTEM
- cpu monit add
- cpu chart add
* Wed Jul 03 2013 alinos <ickhyun.kang@orangecrew.com>
- 0.1.1
- c2sinfo -> ocinfo change
- ocinfo script rpm packaging
* Wed Dec 05 2012 alinos <ickhyun@com2us.com>
- 0.1.0
- c2sinfo script rpm packaging
