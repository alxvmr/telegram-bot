Name: python3-module-telegram-bot
Version: 20.6
Release: alt1

Summary: Python interface for the Telegram Bot API
License: LGPLv3
Group: Development/Python
Url: https://pypi.org/project/python-telegram-bot/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/telegram
%python3_sitelibdir/python_telegram_bot-%version.dist-info

%changelog
* Tue Mar 12 2024 Maria Alexeeva <alxvmr@altlinux.org> 20.6-alt1
- 20.6 released

* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.15-alt1
- 13.15 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.14-alt1
- 13.14 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.1-alt1
- 13.1 released

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.1.0-alt1
- initial
