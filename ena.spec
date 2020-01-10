%define kmod_name		ena
%define kmod_vendor		redhat
%define kmod_driver_version	2.0.2K_dup7.6
%define kmod_driver_epoch	%{nil}
%define kmod_rpm_release	2
%define kmod_kernel_version	3.10.0-957.el7
%define kmod_kernel_version_min	%{nil}
%define kmod_kernel_version_dep	%{nil}
%define kmod_kbuild_dir		drivers/net/ethernet/amazon/ena
%define kmod_dependencies       %{nil}
%define kmod_build_dependencies	%{nil}
%define kmod_devel_package	0
%define kmod_install_path	extra/kmod-redhat-ena

%{!?dist: %define dist .el7_6}
%{!?make_build: %define make_build make}

%if "%{kmod_kernel_version_dep}" == ""
%define kmod_kernel_version_dep %{kmod_kernel_version}
%endif

Source0:	%{kmod_name}-%{kmod_vendor}-%{kmod_driver_version}.tar.bz2
# Source code patches
Patch0:	_RHEL7_01-28_net_ena_Eliminate_duplicate_barriers_on_weakly-ordered_ar.patch
Patch1:	_RHEL7_02-28_net_ena_Fix_use_of_uninitialized_DMA_address_bits_field.patch
Patch2:	_RHEL7_03-28_net_ena_fix_surprise_unplug_NULL_dereference_kernel_crash.patch
Patch3:	_RHEL7_04-28_net_ena_fix_driver_when_PAGE_SIZE_==_64kB.patch
Patch4:	_RHEL7_05-28_net_ena_fix_device_destruction_to_gracefully_free_resourc.patch
Patch5:	_RHEL7_06-28_net_ena_fix_potential_double_ena_destroy_device_.patch
Patch6:	_RHEL7_07-28_net_ena_fix_missing_lock_during_device_destruction.patch
Patch7:	_RHEL7_08-28_net_ena_fix_missing_calls_to_READ_ONCE.patch
Patch8:	_RHEL7_09-28_net_ena_fix_incorrect_usage_of_memory_barriers.patch
Patch9:	_RHEL7_10-28_net_ena_remove_ndo_poll_controller.patch
Patch10:	_RHEL7_11-28_net_ena_fix_warning_in_rmmod_caused_by_double_iounmap.patch
Patch11:	_RHEL7_12-28_net_ena_fix_rare_bug_when_failed_restart-resume_is_follow.patch
Patch12:	_RHEL7_13-28_net_ena_fix_NULL_dereference_due_to_untimely_napi_initial.patch
Patch13:	_RHEL7_14-28_net_ena_fix_auto_casting_to_boolean.patch
Patch14:	_RHEL7_15-28_net_ena_minor_performance_improvement.patch
Patch15:	_RHEL7_16-28_net_ena_complete_host_info_to_match_latest_ENA_spec.patch
Patch16:	_RHEL7_17-28_net_ena_introduce_Low_Latency_Queues_data_structures_acco.patch
Patch17:	_RHEL7_18-28_net_ena_add_functions_for_handling_Low_Latency_Queues_in_.patch
Patch18:	_RHEL7_19-28_net_ena_add_functions_for_handling_Low_Latency_Queues_in_.patch
Patch19:	_RHEL7_20-28_net_ena_use_CSUM_CHECKED_device_indication_to_report_skb..patch
Patch20:	_RHEL7_21-28_net_ena_explicit_casting_and_initialization,_and_clearer_.patch
Patch21:	_RHEL7_22-28_net_ena_limit_refill_Rx_threshold_to_256_to_avoid_latency.patch
Patch22:	_RHEL7_23-28_net_ena_change_rx_copybreak_default_to_reduce_kernel_memo.patch
Patch23:	_RHEL7_24-28_net_ena_remove_redundant_parameter_in_ena_com_admin_init_.patch
Patch24:	_RHEL7_25-28_net_ena_update_driver_version_to_2.0.1.patch
Patch25:	_RHEL7_26-28_net_ena_fix_indentations_in_ena_defs_for_better_readabili.patch
Patch26:	_RHEL7_28-28_net_ena_enable_Low_Latency_Queues.patch
Patch27:	0029-force-enable-ENA_ETHERNET.patch
Patch28:	0030-version-bump.patch
Patch29:	_RHEL7_29-31_net_ena_fix_crash_during_failed_resume_from_hibernation.patch
Patch30:	_RHEL7_30-31_net_ena_fix_crash_during_ena_remove_.patch
Patch31:	_RHEL7_31-31_net_ena_update_driver_version_from_2.0.1_to_2.0.2.patch

%define findpat %( echo "%""P" )
%define __find_requires /usr/lib/rpm/redhat/find-requires.ksyms
%define __find_provides /usr/lib/rpm/redhat/find-provides.ksyms %{kmod_name} %{?epoch:%{epoch}:}%{version}-%{release}
%define sbindir %( if [ -d "/sbin" -a \! -h "/sbin" ]; then echo "/sbin"; else echo %{_sbindir}; fi )
%define dup_state_dir %{_localstatedir}/lib/rpm-state/kmod-dups
%define kver_state_dir %{dup_state_dir}/kver
%define kver_state_file %{kver_state_dir}/%{kmod_kernel_version}.%(arch)
%define dup_module_list %{dup_state_dir}/rpm-kmod-%{kmod_name}-modules

Name:		kmod-redhat-ena
Version:	%{kmod_driver_version}
Release:	%{kmod_rpm_release}%{?dist}
%if "%{kmod_driver_epoch}" != ""
Epoch:		%{kmod_driver_epoch}
%endif
Summary:	ena module for Driver Update Program
Group:		System/Kernel
License:	GPLv2
URL:		http://www.kernel.org/
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	kernel-devel = %{kmod_kernel_version} redhat-rpm-config kernel-abi-whitelists
ExclusiveArch:	x86_64
%global kernel_source() /usr/src/kernels/%{kmod_kernel_version}.$(arch)

%global _use_internal_dependency_generator 0
%if "%{?kmod_kernel_version_min}" != ""
Provides:	kernel-modules >= %{kmod_kernel_version_min}.%{_target_cpu}
%else
Provides:	kernel-modules = %{kmod_kernel_version_dep}.%{_target_cpu}
%endif
Provides:	kmod-%{kmod_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):	%{sbindir}/weak-modules
Requires(postun):	%{sbindir}/weak-modules
Requires:	kernel >= 3.10.0-957.el7
Requires:	kernel < 3.10.0-958.el7
%if 0
Requires: firmware(%{kmod_name}) = ENTER_FIRMWARE_VERSION
%endif
%if "%{kmod_build_dependencies}" != ""
BuildRequires:  %{kmod_build_dependencies}
%endif
%if "%{kmod_dependencies}" != ""
Requires:       %{kmod_dependencies}
%endif
# if there are multiple kmods for the same driver from different vendors,
# they should conflict with each other.
Conflicts:	kmod-%{kmod_name}

%description
ena module for Driver Update Program

%if 0

%package -n kmod-redhat-ena-firmware
Version:	ENTER_FIRMWARE_VERSION
Summary:	ena firmware for Driver Update Program
Provides:	firmware(%{kmod_name}) = ENTER_FIRMWARE_VERSION
%if "%{kmod_kernel_version_min}" != ""
Provides:	kernel-modules >= %{kmod_kernel_version_min}.%{_target_cpu}
%else
Provides:	kernel-modules = %{kmod_kernel_version_dep}.%{_target_cpu}
%endif
%description -n  kmod-redhat-ena-firmware
ena firmware for Driver Update Program


%files -n kmod-redhat-ena-firmware
%defattr(644,root,root,755)
%{FIRMWARE_FILES}

%endif

# Development package
%if 0%{kmod_devel_package}
%package -n kmod-redhat-ena-devel
Version:	%{kmod_driver_version}
Requires:	kernel >= 3.10.0-957.el7
Requires:	kernel < 3.10.0-958.el7
Summary:	ena development files for Driver Update Program

%description -n  kmod-redhat-ena-devel
ena development files for Driver Update Program


%files -n kmod-redhat-ena-devel
%defattr(644,root,root,755)
/usr/share/kmod-%{kmod_vendor}-%{kmod_name}/Module.symvers
%endif

%post
modules=( $(find /lib/modules/%{kmod_kernel_version}.%(arch)/%{kmod_install_path} | grep '\.ko$') )
printf '%s\n' "${modules[@]}" | %{sbindir}/weak-modules --add-modules --no-initramfs

mkdir -p "%{kver_state_dir}"
touch "%{kver_state_file}"

exit 0

%posttrans
# We have to re-implement part of weak-modules here because it doesn't allow
# calling initramfs regeneration separately
if [ -f "%{kver_state_file}" ]; then
	kver_base="%{kmod_kernel_version_dep}"
	kvers=$(ls -d "/lib/modules/${kver_base%%.*}"*)

	for k_dir in $kvers; do
		k="${k_dir#/lib/modules/}"

		tmp_initramfs="/boot/initramfs-$k.tmp"
		dst_initramfs="/boot/initramfs-$k.img"

		# The same check as in weak-modules: we assume that the kernel present
		# if the symvers file exists.
		if [ -e "/boot/symvers-$k.gz" ]; then
			/usr/bin/dracut -f "$tmp_initramfs" "$k" || exit 1
			cmp -s "$tmp_initramfs" "$dst_initramfs"
			if [ "$?" = 1 ]; then
				mv "$tmp_initramfs" "$dst_initramfs"
			else
				rm -f "$tmp_initramfs"
			fi
		fi
	done

	rm -f "%{kver_state_file}"
	rmdir "%{kver_state_dir}" 2> /dev/null
fi

rmdir "%{dup_state_dir}" 2> /dev/null

exit 0

%preun
if rpm -q --filetriggers kmod 2> /dev/null| grep -q "Trigger for weak-modules call on kmod removal"; then
	mkdir -p "%{kver_state_dir}"
	touch "%{kver_state_file}"
fi

mkdir -p "%{dup_state_dir}"
rpm -ql kmod-redhat-ena-%{kmod_driver_version}-%{kmod_rpm_release}%{?dist}.$(arch) | \
	grep '\.ko$' > "%{dup_module_list}"

%postun
if rpm -q --filetriggers kmod 2> /dev/null| grep -q "Trigger for weak-modules call on kmod removal"; then
	initramfs_opt="--no-initramfs"
else
	initramfs_opt=""
fi

modules=( $(cat "%{dup_module_list}") )
rm -f "%{dup_module_list}"
printf '%s\n' "${modules[@]}" | %{sbindir}/weak-modules --remove-modules $initramfs_opt

rmdir "%{dup_state_dir}" 2> /dev/null

exit 0

%files
%defattr(644,root,root,755)
/lib/modules/%{kmod_kernel_version}.%(arch)
/etc/depmod.d/%{kmod_name}.conf
/usr/share/doc/kmod-%{kmod_name}/greylist.txt

%prep
%setup -n %{kmod_name}-%{kmod_vendor}-%{kmod_driver_version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
rm -rf obj
cp -r source obj
%{make_build} -C %{kernel_source} V=1 M=$PWD/obj/%{kmod_kbuild_dir} \
	NOSTDINC_FLAGS="-I $PWD/obj/include -I $PWD/obj/include/uapi" \
	EXTRA_CFLAGS="%{nil}" \
	%{nil}
# mark modules executable so that strip-to-file can strip them
find obj/%{kmod_kbuild_dir} -name "*.ko" -type f -exec chmod u+x '{}' +

whitelist="/lib/modules/kabi-current/kabi_whitelist_%{_target_cpu}"
for modules in $( find obj/%{kmod_kbuild_dir} -name "*.ko" -type f -printf "%{findpat}\n" | sed 's/\.ko$//' | sort -u ) ; do
	# update depmod.conf
	module_weak_path=$(echo "$modules" | sed 's/[\/]*[^\/]*$//')
	if [ -z "$module_weak_path" ]; then
		module_weak_path=%{name}
	else
		module_weak_path=%{name}/$module_weak_path
	fi
	echo "override $(echo $modules | sed 's/.*\///')" \
	     "$(echo "%{kmod_kernel_version_dep}" |
	        sed 's/\.[^\.]*$//;
		     s/\([.+?^$\/\\|()\[]\|\]\)/\\\0/g').*" \
		     "weak-updates/$module_weak_path" >> source/depmod.conf

	# update greylist
	nm -u obj/%{kmod_kbuild_dir}/$modules.ko | sed 's/.*U //' |  sed 's/^\.//' | sort -u | while read -r symbol; do
		grep -q "^\s*$symbol\$" $whitelist || echo "$symbol" >> source/greylist
	done
done
sort -u source/greylist | uniq > source/greylist.txt

%install
export INSTALL_MOD_PATH=$RPM_BUILD_ROOT
export INSTALL_MOD_DIR=%{kmod_install_path}
make -C %{kernel_source} modules_install \
	M=$PWD/obj/%{kmod_kbuild_dir}
# Cleanup unnecessary kernel-generated module dependency files.
find $INSTALL_MOD_PATH/lib/modules -iname 'modules.*' -exec rm {} \;

install -m 644 -D source/depmod.conf $RPM_BUILD_ROOT/etc/depmod.d/%{kmod_name}.conf
install -m 644 -D source/greylist.txt $RPM_BUILD_ROOT/usr/share/doc/kmod-%{kmod_name}/greylist.txt
%if 0
%{FIRMWARE_FILES_INSTALL}
%endif
%if 0%{kmod_devel_package}
install -m 644 -D $PWD/obj/%{kmod_kbuild_dir}/Module.symvers $RPM_BUILD_ROOT/usr/share/kmod-%{kmod_vendor}-%{kmod_name}/Module.symvers
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Dec 19 2018 Eugene Syromiatnikov <esyr@redhat.com> 2.0.2K_dup7.6-2
- baf6ab56eb2d596f7d4c6c1e1ccd8a73db6e1c94
- Resolves: #bz1659505
- ena module for Driver Update Program
