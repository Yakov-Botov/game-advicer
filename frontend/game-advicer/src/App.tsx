import React, { useCallback, useState } from 'react'
import '@vkontakte/vkui/dist/vkui.css'

import {
    AppPanelsIds,
    RandomGamePanel,
    FavoriteListPanel,
    ProfilePanel,
} from './core/panels'
import { Tabbar, Epic, View, TabbarItem } from '@vkontakte/vkui'
import { IconsAdapter } from './shared/components'

const App = () => {
    const [activeStory, setActiveStory] = useState<AppPanelsIds>(
        AppPanelsIds.RandomGame
    )

    const handleChangeActiveStory = useCallback(
        (e: React.MouseEvent<HTMLElement>) => {
            if (e?.currentTarget?.dataset?.story) {
                const story = e.currentTarget.dataset.story
                setActiveStory(story as AppPanelsIds)
            }
        },
        []
    )

    return (
        <Epic
            activeStory={activeStory}
            tabbar={
                <Tabbar>
                    <TabbarItem
                        onClick={handleChangeActiveStory}
                        selected={activeStory === AppPanelsIds.FavoriteList}
                        data-story={AppPanelsIds.FavoriteList}
                        text="Понравившиеся"
                    >
                        <IconsAdapter iconType={'Icon28LikeOutline'} />
                    </TabbarItem>
                    <TabbarItem
                        onClick={handleChangeActiveStory}
                        selected={activeStory === AppPanelsIds.RandomGame}
                        data-story={AppPanelsIds.RandomGame}
                        text="Случайная игра"
                    >
                        <IconsAdapter iconType={'Icon28GameOutline'} />
                    </TabbarItem>
                    <TabbarItem
                        onClick={handleChangeActiveStory}
                        selected={activeStory === AppPanelsIds.Profile}
                        data-story={AppPanelsIds.Profile}
                        text="Профиль"
                    >
                        <IconsAdapter iconType={'Icon28UserCircleOutline'} />
                    </TabbarItem>
                </Tabbar>
            }
        >
            <View
                id={AppPanelsIds.FavoriteList}
                activePanel={AppPanelsIds.FavoriteList}
            >
                <FavoriteListPanel id={AppPanelsIds.FavoriteList} />
            </View>
            <View
                id={AppPanelsIds.RandomGame}
                activePanel={AppPanelsIds.RandomGame}
            >
                <RandomGamePanel id={AppPanelsIds.RandomGame} />
            </View>
            <View id={AppPanelsIds.Profile} activePanel={AppPanelsIds.Profile}>
                <ProfilePanel id={AppPanelsIds.Profile} />
            </View>
        </Epic>
    )
}

export default App
