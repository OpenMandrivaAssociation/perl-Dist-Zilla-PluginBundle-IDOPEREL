%define upstream_name    Dist-Zilla-PluginBundle-IDOPEREL
%define upstream_version 0.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	IDOPEREL's plugin bundle for Dist::Zilla
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::Plugin::AutoPrereq)
BuildRequires:	perl(Dist::Zilla::Plugin::GithubMeta)
BuildRequires:	perl(Dist::Zilla::Plugin::MetaJSON)
BuildRequires:	perl(Dist::Zilla::Plugin::MinimumPerl)
BuildRequires:	perl(Dist::Zilla::Plugin::NextRelease)
BuildRequires:	perl(Dist::Zilla::Plugin::ReadmeFromPod)
BuildRequires:	perl(Dist::Zilla::Plugin::TestRelease)
BuildRequires:	perl(Dist::Zilla::PluginBundle::Classic)
BuildRequires:	perl(Dist::Zilla::PluginBundle::Filter)
BuildRequires:	perl(Dist::Zilla::PluginBundle::Git)
BuildRequires:	perl(Dist::Zilla::Role::PluginBundle)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
This module is a bundle of plugins for the Dist::Zilla manpage that is
regularly used by me (Ido Perlmuter). If you find it suits your needs, feel
free to install and use it.

This bundle provides the following plugins and bundles:

	[@Filter]
	-bundle = @Classic
	-remove = Readme

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml LICENSE META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

