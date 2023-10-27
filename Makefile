.PHONY: install test run clean

# Install the required packages
install:
	@echo "Installing required packages..."
	pip install -r requirements.txt

# Run the tests
test:
	@echo "Running tests..."
	python -m unittest discover tests

# Run the main application
run:
	@echo "Running the main application..."
	python src/main.py

# Clean up any pyc files
clean:
	@echo "Cleaning up..."
	find . -name "*.pyc" -exec rm -f {} \;
