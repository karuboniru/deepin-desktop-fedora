# Generated by go2rpm 1
%bcond_without check

# https://github.com/rickb777/plural
%global goipath         github.com/rickb777/plural
Version:                1.2.0

%gometa

%global common_description %{expand:
Simple Go API for pluralisation.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple Go API for pluralisation

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Thu May 07 00:09:26 CST 2020 Robin Lee <robinlee.sysu@gmail.com> - 1.2.0-1
- Initial package
