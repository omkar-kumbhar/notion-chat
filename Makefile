# Makefile for common Git operations

# Variables
B ?= new-branch
M ?= "Update"
LOG_FILE := git_operations.log

# Targets

status:
	@echo "makeOps: Checking git status..." | tee -a $(LOG_FILE)
	@echo "Timestamp: `date`" >> $(LOG_FILE)
	@git status | tee -a $(LOG_FILE)

checkout:
	@echo "makeOps: Checking out to branch $(B)..." | tee -a $(LOG_FILE)
	@echo "Timestamp: `date`" >> $(LOG_FILE)
	@git checkout $(B) | tee -a $(LOG_FILE)

new-branch:
	@echo "makeOps: Creating and checking out to new branch $(B)..." | tee -a $(LOG_FILE)
	@echo "Timestamp: `date`" >> $(LOG_FILE)
	@git checkout -b $(B) | tee -a $(LOG_FILE)

pull:
	@echo "makeOps: Pulling latest changes from branch $(B)..." | tee -a $(LOG_FILE)
	@echo "Timestamp: `date`" >> $(LOG_FILE)
	@git pull origin $(B) | tee -a $(LOG_FILE)

push:
	@echo "makeOps: Pushing to branch $(B)..." | tee -a $(LOG_FILE)
	@echo "Timestamp: `date`" >> $(LOG_FILE)
	@git push origin $(B) | tee -a $(LOG_FILE)

commit:
	@echo "makeOps: Committing with message: $(M)" | tee -a $(LOG_FILE)
	@echo "Timestamp: `date`" >> $(LOG_FILE)
	@git add . 
	@git commit -m $(M) | tee -a $(LOG_FILE)

all: commit push

help:
	@echo "Makefile for common Git operations"
	@echo
	@echo "Usage:"
	@echo "  make status                 # Show the status of the repository"
	@echo "  make checkout B=branch_name  # Checkout to a branch"
	@echo "  make new-branch B=branch_name # Create and checkout to a new branch"
	@echo "  make pull B=branch_name       # Pull from a branch"
	@echo "  make push B=branch_name       # Push to a branch"
	@echo "  make commit M='Your commit message' # Add all changes and commit"
	@echo "  make all M='Your commit message'   # Commit all changes and push"
	@echo "  make help                   # Show this help message"

.PHONY: status checkout new-branch pull push commit all help
