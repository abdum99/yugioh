DOWNLOAD := res/db/cards.json res/db/sets.json
SET2CARDS := res/db/sets2cards.json

.PHONY: all setup build clean remove update mount unmount

all: $(DOWNLOAD) $(SET2CARDS)
	# Done now run ./install_set.sh SET_NAME to install a set
	# SET_NAME must be from https://ygoprodeck.com/packs/

$(SET2CARDS): $(DOWNLOAD)
	python3 scripts/build_db.py

build: $(SET2CARDS)

$(DOWNLOAD):
	python3 -m pip install -r requirements.txt
	python3 scripts/db_crawler.py

remove:
	rm -f $(DOWNLOAD)

destroy:
	rm -f $(SET2CARDS)

clean: remove destroy

update: clean all

# SSHFS to speed development
mount:
	echo ${RPI_PASSWORD} | sshfs -o password_stdin ${RPI_USERNAME}@${RPI_HOST}:${RPI_REMOTE_PATH} ${DUEL_DISK_PATH}/rpi

unmount:
	umount ${DUEL_DISK_PATH}/rpi

