### RPM external cmake 2.8.1
%define downloaddir %(echo %realversion | cut -d. -f1,2)
Source: http://www.cmake.org/files/v%{downloaddir}/%n-%realversion.tar.gz
%define closingbrace )
%define online %(case %cmsplatf in *onl_*_*%closingbrace echo true;; *%closingbrace echo false;; esac)
#Patch1: cmake
Patch2: cmake-osx-nld

#We are using system zlib for the online builds:
%if "%online" != "true"
Requires: zlib
%endif

%prep

%setup -n cmake-%realversion
# This patch disables the warning about long doubles that some
# macosx compilers emit. Even if it matters only for macosx,
# we apply it anyway to avoid discrepancies and to avoid that 
# it's left behind if cmake version is changed. 
%patch2 -p1

%build
./configure --prefix=%i
make %makeprocesses
