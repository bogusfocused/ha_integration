from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import HomeAssistantType

async def async_setup(hass: HomeAssistantType, config: ConfigType):
    """Initialize the platform."""
    return True

async def async_setup_entry(hass: HomeAssistantType, entry: ConfigEntry):
    return True

