#
# $Id$
#
%define perlvendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define srcname rpmbootstrap

Summary:	rpmbootstrap is a tool similar to debootstrap for RPM based distributions
Summary(fr):	rpmbootstrap crée un environnement chrooté pour la distribution concernée

Name:		rpmbootstrap
Version:	0.9.10
Release:	%mkrel 1
License:	GPL
Group:		System/Configuration/Packaging
Url:		http://trac.project-builder.org
Source:		ftp://ftp.project-builder.org/src/%{srcname}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
BuildArch:	noarch
Requires:	perl >= 5.8.4,perl-ProjectBuilder,perl-libwww-perl, 

%description
rpmbootstrap is a tool similar to debootstrap for RPM based distributions.
It helps building a chrooted environment for the related distribution

%description -l fr
rpmbootstrap crée un environnement chrooté pour la distribution concernée
Il est similaire à debootstrap pour les distributions .deb

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor destdir=${RPM_BUILD_ROOT}/ 
make

%install
%{__rm} -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
find ${RPM_BUILD_ROOT} -type f -name perllocal.pod -o -name .packlist -o -name '*.bs' -a -size 0 | xargs rm -f
find ${RPM_BUILD_ROOT} -type d -depth | xargs rmdir --ignore-fail-on-non-empty

%check
make test

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS AUTHORS
%doc INSTALL COPYING README

#%{perlvendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
#%{_mandir}/man3/*
