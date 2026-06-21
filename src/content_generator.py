"""
Core content generation engine using LLMs and viral pattern templates.
Generates BookTok and wellness content optimized for TikTok and Instagram Reels.
"""

import json
import random
from typing import List, Dict, Any
from datetime import datetime
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

try:
    from anthropic import Anthropic
except ImportError:
    Anthropic = None


class ContentGenerator:
    """Generates viral social media content based on hooks, patterns, and brand voice."""

    def __init__(self, config_path: str = "config/brand_config.json", use_api: str = "openai"):
        """
        Initialize content generator.
        
        Args:
            config_path: Path to brand configuration
            use_api: "openai" or "anthropic"
        """
        self.config = self._load_config(config_path)
        self.booktok_hooks = self._load_hooks("data/booktok_hooks.json")
        self.wellness_hooks = self._load_hooks("data/wellness_hooks.json")
        self.use_api = use_api
        self.client = self._init_client()

    def _load_config(self, path: str) -> Dict:
        """Load brand configuration."""
        with open(path, 'r') as f:
            return json.load(f)

    def _load_hooks(self, path: str) -> Dict:
        """Load hook templates."""
        with open(path, 'r') as f:
            return json.load(f)

    def _init_client(self):
        """Initialize LLM client."""
        if self.use_api == "openai" and OpenAI:
            return OpenAI()
        elif self.use_api == "anthropic" and Anthropic:
            return Anthropic()
        else:
            print(f"Warning: {self.use_api} client not available")
            return None

    def generate_booktok_content(
        self,
        count: int = 5,
        format_type: str = None,
        book_title: str = None,
        character_name: str = None,
        product_link: bool = False
    ) -> List[Dict[str, Any]]:
        """
        Generate BookTok content ideas.
        
        Args:
            count: Number of content ideas to generate
            format_type: Specific format
            book_title: Optional specific book
            character_name: Optional specific character
            product_link: Whether to include product links
            
        Returns:
            List of content ideas with scripts and CTAs
        """
        content_ideas = []

        for _ in range(count):
            hooks = self.booktok_hooks["viral_hooks"]
            hook_template = random.choice(hooks)
            hook_category = hook_template["category"]

            idea = {
                "id": f"booktok_{datetime.now().timestamp()}",
                "niche": "booktok",
                "hook_category": hook_category,
                "hook_template": hook_template,
                "duration": "30-45 seconds",
                "platforms": ["tiktok", "instagram_reels"],
                "cta": random.choice(self.booktok_hooks["cta_patterns"]),
                "hashtags": self._generate_hashtags("booktok"),
                "created_at": datetime.now().isoformat()
            }
            content_ideas.append(idea)

        return content_ideas

    def generate_wellness_content(
        self,
        count: int = 5,
        format_type: str = None,
        topic: str = None,
        product_link: bool = False,
        style: str = "motivational"
    ) -> List[Dict[str, Any]]:
        """
        Generate wellness content ideas.
        
        Args:
            count: Number of content ideas to generate
            format_type: Specific format
            topic: Wellness topic
            product_link: Whether to include product links
            style: "motivational", "educational", etc.
            
        Returns:
            List of content ideas with scripts and CTAs
        """
        content_ideas = []

        for _ in range(count):
            hooks = self.wellness_hooks["viral_hooks"]
            hook_template = random.choice(hooks)
            hook_category = hook_template["category"]

            idea = {
                "id": f"wellness_{datetime.now().timestamp()}",
                "niche": "wellness",
                "hook_category": hook_category,
                "hook_template": hook_template,
                "duration": "15-60 seconds",
                "platforms": ["tiktok", "instagram_reels"],
                "cta": random.choice(self.wellness_hooks["cta_patterns"]),
                "hashtags": self._generate_hashtags("wellness"),
                "created_at": datetime.now().isoformat()
            }
            content_ideas.append(idea)

        return content_ideas

    def _generate_hashtags(self, niche: str, count: int = 15) -> List[str]:
        """Generate relevant hashtags for niche."""
        if niche == "booktok":
            hashtags = [
                "#BookTok", "#BookRecommendations", "#ReadMore",
                "#Bookworm", "#AmReading", "#SpicyBooks",
                "#DarkAcademia", "#RomanceReads", "#BookstagramCommunity"
            ]
        else:  # wellness
            hashtags = [
                "#Wellness", "#SelfCare", "#MentalHealth",
                "#WellnessJourney", "#HealthyHabits", "#Mindfulness",
                "#FemaleWellness", "#WomensMentalHealth", "#RoutineGoals"
            ]
        
        return hashtags[:count]

    def batch_generate(
        self,
        niches: List[str] = None,
        total_count: int = 10,
        save_to_file: bool = True
    ) -> Dict[str, List[Dict]]:
        """
        Generate content across multiple niches.
        
        Args:
            niches: List of niches ("booktok", "wellness")
            total_count: Total content pieces to generate
            save_to_file: Save generated content to JSON
            
        Returns:
            Dictionary with generated content by niche
        """
        if niches is None:
            niches = ["booktok", "wellness"]

        results = {}
        per_niche = total_count // len(niches)

        for niche in niches:
            if niche == "booktok":
                results["booktok"] = self.generate_booktok_content(count=per_niche, product_link=True)
            elif niche == "wellness":
                results["wellness"] = self.generate_wellness_content(count=per_niche, product_link=True)

        if save_to_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = f"data/generated_content_{timestamp}.json"
            with open(filepath, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"Generated content saved to {filepath}")

        return results


if __name__ == "__main__":
    generator = ContentGenerator()
    print("✅ Content Generator initialized")
