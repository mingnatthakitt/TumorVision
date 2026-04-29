.PHONY: dev install clean build

dev:
	@echo "🚀 Starting TumorVision (Backend + Frontend)..."
	@(cd backend && conda run --no-banner -n tumorvision python main.py) & \
	(cd frontend && npm run dev) & \
	wait

install:
	@echo "📦 Installing Frontend dependencies..."
	@cd frontend && npm install
	@echo "📦 Installing Backend dependencies..."
	@cd backend && conda run --no-banner -n tumorvision pip install -r requirements.txt
	@echo "✅ All dependencies installed!"

build:
	@echo "🔨 Building frontend for production..."
	@cd frontend && npm run build
	@echo "✅ Production build ready in frontend/dist/"

clean:
	@echo "🧹 Cleaning build artifacts..."
	@rm -rf frontend/dist frontend/node_modules/.vite
	@echo "✅ Clean!"
