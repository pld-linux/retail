Summary:	An incremental logfile reader
Summary(pl.UTF-8):	Przyrostowy czytnik logów
Name:		retail
Version:	1.0.1
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.xjack.org/retail/download/%{name}-%{version}.tar.gz
# Source0-md5:	a4ec84367d74efd13a68b7728d69dd80
URL:		http://www.xjack.org/retail/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is an attempt to write an intelligent incremental logfile
reading utility.

In summary, something like the following, if run as a cronjob:
retail /var/log/messages | mail youremail@yourdomain.com
Will get you all the new entries which happen to show up in your
system log.  In addition, it will attempt to intelligently cope with any
changes to the file in question, by verifying that the data at it's last known
position has not changed, and if it has it will search out that same data
wherever in the file it now resides.  Should this be also impossible, it will
resort to rewinding to the beginning of the file and reading the entire thing.

%description -l pl.UTF-8
Przyrostowy czytnik logów.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

# provide also logtail for older apps
ln -sf retail $RPM_BUILD_ROOT%{_bindir}/logtail

mv $RPM_BUILD_ROOT%{_prefix}/man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING TODO INSTALL CREDITS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
