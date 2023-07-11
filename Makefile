mount:
	echo ${RPI_PASSWORD} | sshfs -o password_stdin ${RPI_USERNAME}@${RPI_HOST}:${RPI_REMOTE_PATH} ${DUEL_DISK_PATH}/rpi

unmount:
	umount ${DUEL_DISK_PATH}/rpi
