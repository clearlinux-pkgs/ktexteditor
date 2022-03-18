#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : ktexteditor
Version  : 5.92.0
Release  : 48
URL      : https://download.kde.org/stable/frameworks/5.92/ktexteditor-5.92.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.92/ktexteditor-5.92.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.92/ktexteditor-5.92.0.tar.xz.sig
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
BuildRequires : kauth-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfig-dev
BuildRequires : kguiaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kparts-dev
BuildRequires : ktextwidgets-dev
BuildRequires : sonnet-dev
BuildRequires : syntax-highlighting-dev

%description
indentation in comments should not be touched

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
%setup -q -n ktexteditor-5.92.0
cd %{_builddir}/ktexteditor-5.92.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647635750
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1647635750
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ktexteditor
cp %{_builddir}/ktexteditor-5.92.0/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/ktexteditor/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
cp %{_builddir}/ktexteditor-5.92.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/ktexteditor/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/ktexteditor-5.92.0/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/ktexteditor/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/ktexteditor-5.92.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ktexteditor/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/ktexteditor-5.92.0/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/ktexteditor/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
cp %{_builddir}/ktexteditor-5.92.0/templates/ktexteditor-plugin/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/ktexteditor/20079e8f79713dce80ab09774505773c926afa2a
pushd clr-build
%make_install
popd
%find_lang ktexteditor5

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kauth/kauth_ktexteditor_helper

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/org.kde.ktexteditor.katetextbuffer.service
/usr/share/dbus-1/system.d/org.kde.ktexteditor.katetextbuffer.conf
/usr/share/katepart5/script/README.md
/usr/share/kdevfiletemplates/templates/ktexteditor-plugin.tar.bz2
/usr/share/kservices5/katepart.desktop
/usr/share/kservicetypes5/ktexteditor.desktop
/usr/share/kservicetypes5/ktexteditorplugin.desktop
/usr/share/polkit-1/actions/org.kde.ktexteditor.katetextbuffer.policy
/usr/share/qlogging-categories5/ktexteditor.categories
/usr/share/qlogging-categories5/ktexteditor.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KTextEditor/KTextEditor/AbstractAnnotationItemDelegate
/usr/include/KF5/KTextEditor/KTextEditor/AnnotationInterface
/usr/include/KF5/KTextEditor/KTextEditor/Application
/usr/include/KF5/KTextEditor/KTextEditor/Attribute
/usr/include/KF5/KTextEditor/KTextEditor/CodeCompletionInterface
/usr/include/KF5/KTextEditor/KTextEditor/CodeCompletionModel
/usr/include/KF5/KTextEditor/KTextEditor/CodeCompletionModelControllerInterface
/usr/include/KF5/KTextEditor/KTextEditor/Command
/usr/include/KF5/KTextEditor/KTextEditor/ConfigInterface
/usr/include/KF5/KTextEditor/KTextEditor/ConfigPage
/usr/include/KF5/KTextEditor/KTextEditor/Cursor
/usr/include/KF5/KTextEditor/KTextEditor/Document
/usr/include/KF5/KTextEditor/KTextEditor/DocumentCursor
/usr/include/KF5/KTextEditor/KTextEditor/Editor
/usr/include/KF5/KTextEditor/KTextEditor/InlineNote
/usr/include/KF5/KTextEditor/KTextEditor/InlineNoteInterface
/usr/include/KF5/KTextEditor/KTextEditor/InlineNoteProvider
/usr/include/KF5/KTextEditor/KTextEditor/LineRange
/usr/include/KF5/KTextEditor/KTextEditor/MainWindow
/usr/include/KF5/KTextEditor/KTextEditor/MarkInterface
/usr/include/KF5/KTextEditor/KTextEditor/Message
/usr/include/KF5/KTextEditor/KTextEditor/ModificationInterface
/usr/include/KF5/KTextEditor/KTextEditor/MovingCursor
/usr/include/KF5/KTextEditor/KTextEditor/MovingInterface
/usr/include/KF5/KTextEditor/KTextEditor/MovingRange
/usr/include/KF5/KTextEditor/KTextEditor/MovingRangeFeedback
/usr/include/KF5/KTextEditor/KTextEditor/Plugin
/usr/include/KF5/KTextEditor/KTextEditor/Range
/usr/include/KF5/KTextEditor/KTextEditor/SessionConfigInterface
/usr/include/KF5/KTextEditor/KTextEditor/TextHintInterface
/usr/include/KF5/KTextEditor/KTextEditor/View
/usr/include/KF5/KTextEditor/ktexteditor/abstractannotationitemdelegate.h
/usr/include/KF5/KTextEditor/ktexteditor/annotationinterface.h
/usr/include/KF5/KTextEditor/ktexteditor/application.h
/usr/include/KF5/KTextEditor/ktexteditor/attribute.h
/usr/include/KF5/KTextEditor/ktexteditor/codecompletioninterface.h
/usr/include/KF5/KTextEditor/ktexteditor/codecompletionmodel.h
/usr/include/KF5/KTextEditor/ktexteditor/codecompletionmodelcontrollerinterface.h
/usr/include/KF5/KTextEditor/ktexteditor/command.h
/usr/include/KF5/KTextEditor/ktexteditor/configinterface.h
/usr/include/KF5/KTextEditor/ktexteditor/configpage.h
/usr/include/KF5/KTextEditor/ktexteditor/cursor.h
/usr/include/KF5/KTextEditor/ktexteditor/document.h
/usr/include/KF5/KTextEditor/ktexteditor/documentcursor.h
/usr/include/KF5/KTextEditor/ktexteditor/editor.h
/usr/include/KF5/KTextEditor/ktexteditor/inlinenote.h
/usr/include/KF5/KTextEditor/ktexteditor/inlinenoteinterface.h
/usr/include/KF5/KTextEditor/ktexteditor/inlinenoteprovider.h
/usr/include/KF5/KTextEditor/ktexteditor/linerange.h
/usr/include/KF5/KTextEditor/ktexteditor/mainwindow.h
/usr/include/KF5/KTextEditor/ktexteditor/markinterface.h
/usr/include/KF5/KTextEditor/ktexteditor/message.h
/usr/include/KF5/KTextEditor/ktexteditor/modificationinterface.h
/usr/include/KF5/KTextEditor/ktexteditor/movingcursor.h
/usr/include/KF5/KTextEditor/ktexteditor/movinginterface.h
/usr/include/KF5/KTextEditor/ktexteditor/movingrange.h
/usr/include/KF5/KTextEditor/ktexteditor/movingrangefeedback.h
/usr/include/KF5/KTextEditor/ktexteditor/plugin.h
/usr/include/KF5/KTextEditor/ktexteditor/range.h
/usr/include/KF5/KTextEditor/ktexteditor/sessionconfiginterface.h
/usr/include/KF5/KTextEditor/ktexteditor/texthintinterface.h
/usr/include/KF5/KTextEditor/ktexteditor/view.h
/usr/include/KF5/KTextEditor/ktexteditor_export.h
/usr/include/KF5/KTextEditor/ktexteditor_version.h
/usr/lib64/cmake/KF5TextEditor/KF5TextEditorConfig.cmake
/usr/lib64/cmake/KF5TextEditor/KF5TextEditorConfigVersion.cmake
/usr/lib64/cmake/KF5TextEditor/KF5TextEditorTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5TextEditor/KF5TextEditorTargets.cmake
/usr/lib64/libKF5TextEditor.so
/usr/lib64/qt5/mkspecs/modules/qt_KTextEditor.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5TextEditor.so.5
/usr/lib64/libKF5TextEditor.so.5.92.0
/usr/lib64/qt5/plugins/kf5/parts/katepart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ktexteditor/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/ktexteditor/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/ktexteditor/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/ktexteditor/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3

%files locales -f ktexteditor5.lang
%defattr(-,root,root,-)

