#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: e738c51
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : ktexteditor
Version  : 6.0.0
Release  : 77
URL      : https://download.kde.org/stable/frameworks/6.0/ktexteditor-6.0.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.0/ktexteditor-6.0.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.0/ktexteditor-6.0.0.tar.xz.sig
Summary  : Advanced embeddable text editor
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 LGPL-2.0 MIT
Requires: ktexteditor-data = %{version}-%{release}
Requires: ktexteditor-lib = %{version}-%{release}
Requires: ktexteditor-license = %{version}-%{release}
Requires: ktexteditor-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : karchive-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kguiaddons-dev
BuildRequires : kparts-dev
BuildRequires : qt6base-dev
BuildRequires : sonnet-dev
BuildRequires : syntax-highlighting-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Test if the selection is adjusted correctly when duplicating down.

%package data
Summary: data components for the ktexteditor package.
Group: Data

%description data
data components for the ktexteditor package.


%package dev
Summary: dev components for the ktexteditor package.
Group: Development
Requires: ktexteditor-lib = %{version}-%{release}
Requires: ktexteditor-data = %{version}-%{release}
Provides: ktexteditor-devel = %{version}-%{release}
Requires: ktexteditor = %{version}-%{release}

%description dev
dev components for the ktexteditor package.


%package lib
Summary: lib components for the ktexteditor package.
Group: Libraries
Requires: ktexteditor-data = %{version}-%{release}
Requires: ktexteditor-license = %{version}-%{release}

%description lib
lib components for the ktexteditor package.


%package license
Summary: license components for the ktexteditor package.
Group: Default

%description license
license components for the ktexteditor package.


%package locales
Summary: locales components for the ktexteditor package.
Group: Default

%description locales
locales components for the ktexteditor package.


%prep
%setup -q -n ktexteditor-6.0.0
cd %{_builddir}/ktexteditor-6.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709309164
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1709309164
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ktexteditor
cp %{_builddir}/ktexteditor-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/ktexteditor/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/ktexteditor-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ktexteditor/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/ktexteditor-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/ktexteditor/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/ktexteditor-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ktexteditor/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/ktexteditor-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/ktexteditor/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
cp %{_builddir}/ktexteditor-%{version}/templates/ktexteditor6-plugin/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ktexteditor/20079e8f79713dce80ab09774505773c926afa2a || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang ktexteditor6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf6/kauth/kauth_ktexteditor_helper
/usr/lib64/libexec/kf6/kauth/kauth_ktexteditor_helper

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.kde.ktexteditor6.katetextbuffer.service
/usr/share/dbus-1/system.d/org.kde.ktexteditor6.katetextbuffer.conf
/usr/share/kdevappwizard/templates/ktexteditor6-plugin.tar.bz2
/usr/share/qlogging-categories6/ktexteditor.categories
/usr/share/qlogging-categories6/ktexteditor.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KTextEditor/KTextEditor/AbstractAnnotationItemDelegate
/usr/include/KF6/KTextEditor/KTextEditor/AnnotationInterface
/usr/include/KF6/KTextEditor/KTextEditor/Application
/usr/include/KF6/KTextEditor/KTextEditor/Attribute
/usr/include/KF6/KTextEditor/KTextEditor/CodeCompletionModel
/usr/include/KF6/KTextEditor/KTextEditor/CodeCompletionModelControllerInterface
/usr/include/KF6/KTextEditor/KTextEditor/Command
/usr/include/KF6/KTextEditor/KTextEditor/ConfigPage
/usr/include/KF6/KTextEditor/KTextEditor/Cursor
/usr/include/KF6/KTextEditor/KTextEditor/Document
/usr/include/KF6/KTextEditor/KTextEditor/DocumentCursor
/usr/include/KF6/KTextEditor/KTextEditor/Editor
/usr/include/KF6/KTextEditor/KTextEditor/InlineNote
/usr/include/KF6/KTextEditor/KTextEditor/InlineNoteProvider
/usr/include/KF6/KTextEditor/KTextEditor/LineRange
/usr/include/KF6/KTextEditor/KTextEditor/MainWindow
/usr/include/KF6/KTextEditor/KTextEditor/Message
/usr/include/KF6/KTextEditor/KTextEditor/MovingCursor
/usr/include/KF6/KTextEditor/KTextEditor/MovingRange
/usr/include/KF6/KTextEditor/KTextEditor/MovingRangeFeedback
/usr/include/KF6/KTextEditor/KTextEditor/Plugin
/usr/include/KF6/KTextEditor/KTextEditor/Range
/usr/include/KF6/KTextEditor/KTextEditor/SessionConfigInterface
/usr/include/KF6/KTextEditor/KTextEditor/TextHintInterface
/usr/include/KF6/KTextEditor/KTextEditor/View
/usr/include/KF6/KTextEditor/ktexteditor/abstractannotationitemdelegate.h
/usr/include/KF6/KTextEditor/ktexteditor/annotationinterface.h
/usr/include/KF6/KTextEditor/ktexteditor/application.h
/usr/include/KF6/KTextEditor/ktexteditor/attribute.h
/usr/include/KF6/KTextEditor/ktexteditor/codecompletionmodel.h
/usr/include/KF6/KTextEditor/ktexteditor/codecompletionmodelcontrollerinterface.h
/usr/include/KF6/KTextEditor/ktexteditor/command.h
/usr/include/KF6/KTextEditor/ktexteditor/configpage.h
/usr/include/KF6/KTextEditor/ktexteditor/cursor.h
/usr/include/KF6/KTextEditor/ktexteditor/document.h
/usr/include/KF6/KTextEditor/ktexteditor/documentcursor.h
/usr/include/KF6/KTextEditor/ktexteditor/editor.h
/usr/include/KF6/KTextEditor/ktexteditor/inlinenote.h
/usr/include/KF6/KTextEditor/ktexteditor/inlinenoteprovider.h
/usr/include/KF6/KTextEditor/ktexteditor/linerange.h
/usr/include/KF6/KTextEditor/ktexteditor/mainwindow.h
/usr/include/KF6/KTextEditor/ktexteditor/message.h
/usr/include/KF6/KTextEditor/ktexteditor/movingcursor.h
/usr/include/KF6/KTextEditor/ktexteditor/movingrange.h
/usr/include/KF6/KTextEditor/ktexteditor/movingrangefeedback.h
/usr/include/KF6/KTextEditor/ktexteditor/plugin.h
/usr/include/KF6/KTextEditor/ktexteditor/range.h
/usr/include/KF6/KTextEditor/ktexteditor/sessionconfiginterface.h
/usr/include/KF6/KTextEditor/ktexteditor/texthintinterface.h
/usr/include/KF6/KTextEditor/ktexteditor/view.h
/usr/include/KF6/KTextEditor/ktexteditor_export.h
/usr/include/KF6/KTextEditor/ktexteditor_version.h
/usr/lib64/cmake/KF6TextEditor/KF6TextEditorConfig.cmake
/usr/lib64/cmake/KF6TextEditor/KF6TextEditorConfigVersion.cmake
/usr/lib64/cmake/KF6TextEditor/KF6TextEditorTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6TextEditor/KF6TextEditorTargets.cmake
/usr/lib64/libKF6TextEditor.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6TextEditor.so.6.0.0
/V3/usr/lib64/qt6/plugins/kf6/parts/katepart.so
/usr/lib64/libKF6TextEditor.so.6
/usr/lib64/libKF6TextEditor.so.6.0.0
/usr/lib64/qt6/plugins/kf6/parts/katepart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ktexteditor/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/ktexteditor/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/ktexteditor/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/ktexteditor/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3

%files locales -f ktexteditor6.lang
%defattr(-,root,root,-)

