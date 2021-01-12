import React from 'react'
import { Loader } from 'shared/components'
import { LoadingWrapperProps } from './LoadingWrapper.model'

/** Оберка для условного рендера лоадера или дочерних компонентов */
export const LoadingWrapper: React.FC<LoadingWrapperProps> = React.memo(
    ({ isLoading, children }) => {
        return <>{isLoading ? <Loader /> : children}</>
    }
)
