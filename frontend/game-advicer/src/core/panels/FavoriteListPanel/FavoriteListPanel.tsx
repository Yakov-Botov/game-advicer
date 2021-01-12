import { Panel, List } from '@vkontakte/vkui'
import React, { useEffect, useMemo, useState } from 'react'
import { PanelBaseProps } from '..'
import { PanelHeader } from '@vkontakte/vkui'
import { FAVORITES_FETCH_MOCK } from './FavoriteListPanel.const'
import { FavoriteListItem } from './FavoriteListPanel.model'
import { FavoriteItemCell, LoadingWrapper } from 'core/components'
import { IconsAdapter, PlaceholderAdapter } from 'shared/components'

export const FavoriteListPanel: React.FC<PanelBaseProps> = React.memo(
    ({ id }) => {
        const [isLoading, setLoading] = useState(false)
        const [favorites, setFavorites] = useState<FavoriteListItem[]>([])

        useEffect(() => {
            const fetchFavorites = async () => {
                try {
                    setLoading(true)
                    const result = await new Promise((resolve) =>
                        setTimeout(() => resolve(FAVORITES_FETCH_MOCK), 1000)
                    )
                    setFavorites(result as FavoriteListItem[])
                } catch (e) {
                    console.error(e)
                } finally {
                    setLoading(false)
                }
            }
            fetchFavorites()
        }, [])

        const favoriteItemsListRender = useMemo(
            () => (
                <List>
                    {favorites.map((item) => (
                        <FavoriteItemCell
                            key={item.id}
                            description={item.genre}
                        >
                            {item.name}
                        </FavoriteItemCell>
                    ))}
                </List>
            ),
            [favorites]
        )

        /** TODO: нужно реализовать DnD внутри списка для того, чтобы юзер имел возможность самостоятельно задавать порядок */
        return (
            <Panel id={id}>
                <PanelHeader>Список понравившихся</PanelHeader>
                <LoadingWrapper isLoading={isLoading}>
                    {favorites.length ? (
                        favoriteItemsListRender
                    ) : (
                        <PlaceholderAdapter
                            stretched
                            icon={
                                <IconsAdapter iconType={'IconStars3Outlined'} />
                            }
                        >
                            У вас еще нет игр в списке понравившихся
                        </PlaceholderAdapter>
                    )}
                </LoadingWrapper>
            </Panel>
        )
    }
)
