#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : ktexteditor
Version  : 5.67.0
Release  : 27
URL      : https://download.kde.org/stable/frameworks/5.67/ktexteditor-5.67.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.67/ktexteditor-5.67.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.67/ktexteditor-5.67.0.tar.xz.sig
Summary  : Advanced embeddable text editor
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: ktexteditor-data = %{version}-%{release}
Requires: ktexteditor-lib = %{version}-%{release}
Requires: ktexteditor-license = %{version}-%{release}
Requires: ktexteditor-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(libgit2)
BuildRequires : karchive-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kguiaddons-dev
BuildRequires : kparts-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : sonnet-dev
BuildRequires : syntax-highlighting-dev

%description
test if after duplicating a line down the lower line has the cursor in it

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
%setup -q -n ktexteditor-5.67.0
cd %{_builddir}/ktexteditor-5.67.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581384681
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581384681
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ktexteditor
cp %{_builddir}/ktexteditor-5.67.0/COPYING.GPL-2 %{buildroot}/usr/share/package-licenses/ktexteditor/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/ktexteditor-5.67.0/COPYING.LGPL-2 %{buildroot}/usr/share/package-licenses/ktexteditor/ba8966e2473a9969bdcab3dc82274c817cfd98a1
cp %{_builddir}/ktexteditor-5.67.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/ktexteditor/9a1929f4700d2407c70b507b3b2aaf6226a9543c
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
/usr/share/kdevappwizard/templates/ktexteditor-plugin.tar.bz2
/usr/share/kservices5/katepart.desktop
/usr/share/kservicetypes5/ktexteditor.desktop
/usr/share/kservicetypes5/ktexteditorplugin.desktop
/usr/share/polkit-1/actions/org.kde.ktexteditor.katetextbuffer.policy
/usr/share/qlogging-categories5/ktexteditor.categories

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
/usr/include/KF5/ktexteditor_version.h
/usr/lib64/cmake/KF5TextEditor/KF5TextEditorConfig.cmake
/usr/lib64/cmake/KF5TextEditor/KF5TextEditorConfigVersion.cmake
/usr/lib64/cmake/KF5TextEditor/KF5TextEditorTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5TextEditor/KF5TextEditorTargets.cmake
/usr/lib64/libKF5TextEditor.so
/usr/lib64/qt5/mkspecs/modules/qt_KTextEditor.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5TextEditor.so.5
/usr/lib64/libKF5TextEditor.so.5.67.0
/usr/lib64/qt5/plugins/kf5/parts/katepart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ktexteditor/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/ktexteditor/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/ktexteditor/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f ktexteditor5.lang
%defattr(-,root,root,-)

