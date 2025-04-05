#!/bin/sh

          for i in {1..15}; do
            echo "Checking if Django is up ($i/15)..."
            if curl -s --fail http://localhost > /dev/null; then
              echo "Django is ready!"
              exit 0
            fi
            echo "Django is not ready yet..."
            sleep 2
          done
          echo "Django failed to start in time." >&2
          docker compose logs web
          exit 1
