Summary:	PHP very user-friendly CAPTCHA solution
Name:		php-captchaphp
Version:	2.3
Release:	1
# Public Domain or any FOSS License, see README
# We're choosing MIT because it is universally compatible with other FOSS licenses.
License:	Public Domain or MIT
Group:		Libraries
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/php-captchaphp/captcha-%{version}.nofont.tar.gz/a950d23c7733ec1ddb40c5df06e1e605/captcha-%{version}.nofont.tar.gz
# Source0-md5:	a950d23c7733ec1ddb40c5df06e1e605
URL:		http://freshmeat.net/projects/captchaphp/
Patch1:		captcha-2.3-24pre.patch
Requires:	php(gd)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		fontdir	%{_datadir}/fonts/TTF

%description
This PHP script provides a very user-friendly CAPTCHA solution. You
can easily embed it into your <form> generation scripts to prevent
spam-bot access.

It strives to be accessible and implements an arithmetic riddle as
alternative for visually impaired users. It does not require cookies,
but makes use of "AJAX" to give users visual feedback for solving the
CAPTCHA. It grants access fuzzily (when single letters were
outguessed) instead of frustrating people. And it can be customized
rather easily.

%prep
%setup -q -n captcha-%{version}
%patch1 -p1

# Replace the font path by our (arbitrary) default font directory.
sed -i -e "/CAPTCHA_FONT_DIR/s#,.*#, '%{fontdir}/');#" captcha.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/captchaphp
cp -p captcha.php $RPM_BUILD_ROOT%{php_data_dir}/captchaphp

%clean
rm -rf "${RPM_BUILD_ROOT}"

%files
%defattr(644,root,root,755)
%doc README index.php
%{php_data_dir}/captchaphp
